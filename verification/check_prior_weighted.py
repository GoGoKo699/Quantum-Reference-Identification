"""Finite occupation, posterior, and Helstrom checks for prior-weighted identification."""

from fractions import Fraction
from math import comb, prod, sqrt

import numpy as np


def occupations(copies, dimension):
    if dimension == 1:
        yield (copies,)
        return
    for first in range(copies + 1):
        for tail in occupations(copies - first, dimension - 1):
            yield (first, *tail)


def posterior(training_copies, query_copies, dimension, training_state):
    m, t, d = training_copies, query_copies, dimension
    train = list(occupations(m, d))
    query = list(occupations(t, d))
    combined = {occ: i for i, occ in enumerate(occupations(m + t, d))}
    embedding = np.zeros((len(train), len(query), len(combined)))
    for i, train_occ in enumerate(train):
        for j, query_occ in enumerate(query):
            occ = tuple(x + y for x, y in zip(train_occ, query_occ))
            weight = prod(comb(x, y) for x, y in zip(occ, train_occ))
            embedding[i, j, combined[occ]] = sqrt(weight / comb(m + t, m))
    result = np.einsum('ij,ika,jla->kl', training_state.T, embedding, embedding)
    return result * (len(train) / len(combined))


def check_posteriors():
    rng = np.random.default_rng(379)
    count = 0
    for d, m, t in [(2, 1, 1), (2, 2, 2), (2, 2, 3), (3, 1, 2), (3, 3, 2), (4, 2, 3)]:
        dm, dt, dmt = (comb(d + k - 1, k) for k in (m, t, m + t))
        upper = Fraction(dm, dmt)
        lower = upper / comb(m + t, m)
        query = list(occupations(t, d))
        train = list(occupations(m, d))
        u = train.index((m, 0, *([0] * (d - 2))))
        v = train.index((0, m, *([0] * (d - 2))))
        query_v = query.index((0, t, *([0] * (d - 2))))
        pure_u = np.outer(np.eye(dm)[u], np.eye(dm)[u])
        pure_v = np.outer(np.eye(dm)[v], np.eye(dm)[v])
        pred_u, pred_v = (posterior(m, t, d, a) for a in (pure_u, pure_v))
        assert abs(pred_u[query_v, query_v] - float(lower)) < 1e-12
        assert abs(pred_v[query_v, query_v] - float(upper)) < 1e-12
        indices = [i for i, occ in enumerate(query) if occ[0] == 0]
        h = Fraction(d - 1, d + t - 1)
        alpha = lower * dt
        assert Fraction(len(indices), dt) == h
        assert abs(np.trace(pred_u[np.ix_(indices, indices)]) - float(h * alpha)) < 1e-12
        for _ in range(8):
            z = rng.normal(size=(dm, 3)) + 1j * rng.normal(size=(dm, 3))
            a = z @ z.conj().T
            prediction = posterior(m, t, d, a / np.trace(a))
            assert abs(np.trace(prediction) - 1) < 1e-12
            eigs = np.linalg.eigvalsh(prediction)
            assert eigs.min() >= float(lower) - 1e-12
            assert eigs.max() <= float(upper) + 1e-12
            count += 1
    return count


def check_helstrom_blocks():
    count = 0
    for m in range(1, 5):
        for t in range(1, 5):
            a, b = m / (m + t), t / (m + t)
            for prior in [(0.49, 0.48, 0.03), (0.6, 0.3, 0.1), (0.8, 0.1, 0.1), (0.98, 0.01, 0.01)]:
                p1, p2, _ = prior
                delta = np.array([[a*p1-p2, sqrt(a*b)*p1], [sqrt(a*b)*p1, b*(p1-p2)]])
                eigs = np.linalg.eigvalsh(delta)
                assert eigs[0] < 0 < eigs[1]
                assert eigs[1] > max(delta[0, 0], 0) + delta[1, 1]
                assert abs(np.linalg.det(delta) - b*p2*(p2-(1+a)*p1)) < 1e-12
                count += 1
    return count


if __name__ == '__main__':
    print(f'Posterior interval: {check_posteriors()} random states, 6 joint endpoint and receiver cases')
    print(f'Strict Helstrom improvement: {check_helstrom_blocks()} prior and copy-count cases')
