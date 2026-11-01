"""Finite checks for supplied-copy quantum reference identification.

This is a verification of selected identities, not a proof or novelty check.
"""
from itertools import permutations, product
from math import comb, exp, log, factorial, lgamma
from functools import lru_cache
from fractions import Fraction
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln
from numpy.polynomial.legendre import leggauss


@lru_cache(maxsize=512)
def _perm_matrix(d, n, perm):
    dim = d ** n
    U = np.zeros((dim, dim))
    for x in product(range(d), repeat=n):
        y = tuple(x[perm[i]] for i in range(n))
        a = sum(x[i] * d ** (n - 1 - i) for i in range(n))
        b = sum(y[i] * d ** (n - 1 - i) for i in range(n))
        U[b, a] = 1
    return U


def perm_matrix(d, n, perm):
    return _perm_matrix(d, n, tuple(perm))


def sym(d, n, indices):
    ans = np.zeros((d ** n, d ** n))
    ps = list(permutations(indices))
    for order in ps:
        p = list(range(n))
        for a, b in zip(indices, order):
            p[a] = b
        ans += perm_matrix(d, n, p)
    return ans / len(ps)


def symmetric_projector(d, n):
    """Occupation-basis construction independent of the permutation average."""
    groups = {}
    for index, word in enumerate(product(range(d), repeat=n)):
        occupation = tuple(word.count(j) for j in range(d))
        groups.setdefault(occupation, []).append(index)
    columns = np.zeros((d**n, len(groups)))
    for j, indices in enumerate(groups.values()):
        columns[indices, j] = 1 / np.sqrt(len(indices))
    return columns @ columns.T, columns


def random_density(n, rng):
    a = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    a = a @ a.conj().T
    return a / np.trace(a)


def posterior_checks(d, m, t, s, rng):
    """Exact finite matrices for arbitrary positive symmetric posterior states.

    A rank-one collective effect on two reference blocks is included by
    reducing one random entangled vector. Such reduced states need not be
    coherent-state mixtures; the moment proof must cover them nonetheless.
    """
    pm, vm = symmetric_projector(d,m)
    pt, _ = symmetric_projector(d,t)
    pmt, _ = symmetric_projector(d,m+t)
    pms, _ = symmetric_projector(d,m*s)
    Dm, Dt, Dmt, Dms = [comb(d+k-1,k) for k in (m,t,m+t,m*s)]
    C = Dm*Dt/Dmt
    alpha = C/comb(m+t,m)
    entangled = rng.normal(size=(Dm,Dm))+1j*rng.normal(size=(Dm,Dm))
    entangled /= np.linalg.norm(entangled)
    reduced = entangled@entangled.conj().T
    small_states = [random_density(Dm,rng), reduced]
    results = []
    for small in small_states:
        a = vm@small@vm.T
        a_power = np.array([[1.]])
        for _ in range(s):
            a_power = np.kron(a_power,a)
        moment_ratio = float(np.trace(a_power@pms).real)
        assert -1e-10 <= moment_ratio <= 1+1e-10
        joint = np.kron(a,np.eye(d**t))@pmt
        posterior = np.einsum('abac->bc',joint.reshape(d**m,d**t,d**m,d**t))*Dm/Dmt
        assert np.linalg.norm(posterior-posterior.conj().T)<1e-10
        assert abs(np.trace(posterior)-1)<1e-10
        minimum = float(np.linalg.eigvalsh(posterior-alpha*pt/Dt).min())
        assert minimum > -1e-10
        results.append({'moment_s':s,'moment_ratio_to_bound':moment_ratio,
                        'common_component_min_eigenvalue':minimum})
    return {'d':d,'m':m,'t':t,'posteriors':results}


def revealed_endpoint(Dm, M):
    """Exact rational optimization of the commuting reference ensemble."""
    direct = Fraction(0)
    for word in product(range(Dm),repeat=M):
        likelihoods = [Fraction(int(word[j]==0),Dm**(M-1)) for j in range(M)]
        direct += max(likelihoods)/M
    formula = Fraction(Dm,M)*(1-(1-Fraction(1,Dm))**M)
    assert direct == formula
    return {'D_m':Dm,'M':M,'exact_optimal_success':str(direct),
            'direct_optimal_success':float(direct),'formula':float(formula)}


def fixed_library_checks(d, m, t, rng):
    """Complex fixed-state acceptance, independently of Haar averaging."""
    a,b=[rng.normal(size=d)+1j*rng.normal(size=d) for _ in range(2)]
    a/=np.linalg.norm(a)
    b/=np.linalg.norm(b)
    overlap=float(abs(np.vdot(a,b))**2)
    state=np.array([1.+0j])
    for v in [a]*m+[b]*t:
        state=np.kron(state,v)
    projector=sym(d,m+t,list(range(m+t)))
    actual=float(np.vdot(state,projector@state).real)
    predicted=sum(comb(m,k)*comb(t,k)*overlap**k
                  for k in range(min(m,t)+1))/comb(m+t,m)
    assert abs(actual-predicted)<1e-12
    return {'d':d,'m':m,'t':t,'overlap':overlap,
            'actual_acceptance':actual,'polynomial_acceptance':predicted}


def haar_quadrature_checks(rng):
    """Independent exact-degree quadrature for qubit posterior identities."""
    nodes,weights=leggauss(20)
    nodes=(nodes+1)/2
    weights/=2
    m=t=2
    Dm=Dt=3
    alpha=3/10
    records=[]
    for sample in range(3):
        vector=rng.normal(size=(Dm,Dm))+1j*rng.normal(size=(Dm,Dm))
        vector/=np.linalg.norm(vector)
        a=vector@vector.conj().T
        moments=np.zeros(6)
        sigma=np.zeros((Dt,Dt),dtype=complex)
        for p,w in zip(nodes,weights):
            for k in range(32):
                phi=2*np.pi*k/32
                v=np.array([np.sqrt(comb(m,j))*p**((m-j)/2)*(1-p)**(j/2)
                            *np.exp(1j*j*phi) for j in range(m+1)])
                q=Dm*float(np.vdot(v,a@v).real)
                moments+=w/32*q**np.arange(1,7)
                sigma+=w/32*q*np.outer(v,v.conj())
        bounds=np.array([Dm**s/(m*s+1) for s in range(1,7)])
        assert abs(moments[0]-1)<1e-12
        assert np.all(moments<=bounds+1e-10)
        assert abs(np.trace(sigma)-1)<1e-12
        residual=float(np.linalg.eigvalsh(sigma-alpha*np.eye(Dt)/Dt)[0])
        assert residual>=-1e-12
        records.append({'sample':sample,'moments_s1_to_s6':moments.tolist(),
                        'moment_upper_bounds':bounds.tolist(),
                        'common_component_residual_min_eigenvalue':residual})
    # A coherent posterior attains all six moment bounds.
    for s in range(1,7):
        value=sum(w*(Dm*p**m)**s for p,w in zip(nodes,weights))
        assert abs(value-Dm**s/(m*s+1))<1e-10
    return {'collective_posteriors':records,'coherent_saturation_s1_to_s6':True}


def log_dimension(d, k):
    return sum(log(d+j) for j in range(k))-lgamma(k+1)


def covariant_asymptotic(log_M, d, m):
    """Deterministic quadrature for E[(max Beta(1,d-1))**m].

    If Z is the maximum of M unit-rate exponentials, X=1-exp(-Z/(d-1))
    is the required beta maximum. Integrate Z-log(M) for numerical stability.
    M is rounded to an integer before evaluating its exact distribution.
    This checks the attaining strategy, not optimality of all training POVMs.
    """
    M = round(exp(log_M))
    log_M = log(M)
    def integrand(v):
        z=v+log_M
        if z<=0:
            return 0.
        e=np.exp(-z)
        density=np.exp(-v+(M-1)*np.log1p(-e))
        x=-np.expm1(-z/(d-1))
        return float(density*x**m)
    moment, error=quad(integrand,max(-log_M,-40),50,epsabs=1e-18,epsrel=2e-10,limit=300)
    scaled_covariant=np.exp(log_dimension(d,m))*moment
    leading=log_M**m/factorial(m)
    smax=max(20,int(4*log_M/m)+10)
    logs=[log_M/s+log_dimension(d,m)-log_dimension(d,m*s)/s for s in range(1,smax+1)]
    converse=np.exp(min(logs))
    assert scaled_covariant <= converse*(1+1e-8)
    return {'log_M':log_M,'d':d,'m':m,'M_times_covariant_success':scaled_covariant,
            'leading_asymptotic':leading,'covariant_to_leading':scaled_covariant/leading,
            'moment_converse_to_leading':converse/leading,
            'best_s':int(np.argmin(logs))+1,'quadrature_error':error}


def finite_covariant_checks():
    rows=[]
    for d,m,M in [(2,1,2),(2,1,7),(3,1,5),(5,2,10),(20,3,25),(100,1,1000)]:
        result=covariant_asymptotic(log(M),d,m)
        success=result['M_times_covariant_success']/M
        row={'d':d,'m':m,'M':M,'covariant_success':success}
        if m==1:
            log_ratio=gammaln(M+1)+gammaln(1+1/(d-1))-gammaln(M+1+1/(d-1))
            gamma_success=d/M*(-np.expm1(log_ratio))
            assert abs(success-gamma_success)<2e-10
            row['m1_gamma_expression']=float(gamma_success)
        rows.append(row)
    return rows


def check(d, M, m, t):
    n = M * m + t
    dim = d ** n
    H = sym(d, n, list(range(t)))
    blocks = [list(range(t + j*m, t + (j+1)*m)) for j in range(M)]
    for block in blocks:
        H = H @ sym(d, n, block)
    L = comb(d+m-1, m) ** M * comb(d+t-1, t)
    C = comb(d+m-1, m) * comb(d+t-1, t) / comb(d+m+t-1, m+t)
    r = L / C
    P = [H @ sym(d, n, list(range(t)) + block) for block in blocks]
    for p in P:
        assert np.linalg.norm(p@p-p) < 1e-9
        assert abs(np.trace(p)-r) < 1e-9
    for i in range(M):
        for j in range(M):
            want = r if i == j else r / C
            assert abs(np.trace(P[i] @ P[j])-want) < 1e-9
            for k in range(M):
                distinct = len({i,j,k})
                want3 = r / C ** (distinct-1)
                assert abs(np.trace(P[i] @ P[j] @ P[k])-want3) < 1e-9
    S = sum(P)
    ev, V = np.linalg.eigh(S)
    w = np.zeros_like(ev)
    w[ev > 1e-10] = ev[ev > 1e-10] ** -0.5
    R = (V * w) @ V.T
    rho = [p/r for p in P]
    E = [R@p@R for p in P]
    pgm = sum(np.trace(e@rr) for e, rr in zip(E,rho))/M
    beta = (M-1)/C
    gamma = (M-1)*(M-2)/C**2
    moments = [np.trace(np.linalg.matrix_power(S,k))/(M*r) for k in range(1,4)]
    assert np.max(np.abs(np.array(moments)-np.array([1,1+beta,1+3*beta+gamma])))<1e-9
    nuclear_success_upper = np.sqrt(np.maximum(ev,0)).sum()/(M*r)
    error_lower = beta/(8+4*(M-2)/C)
    assert 1-nuclear_success_upper+1e-8 >= error_lower
    assert 1-pgm+1e-9 >= error_lower
    optimal_binary = None
    if M == 2:
        optimal_binary = .5+.25*np.abs(np.linalg.eigvalsh(rho[0]-rho[1])).sum()
        assert optimal_binary+1e-9 >= pgm
        assert optimal_binary <= nuclear_success_upper+1e-8
        assert 1-optimal_binary+1e-9 >= error_lower
    sequential = 0.
    prefix = np.eye(dim)
    for j in range(M):
        A = P[j] @ prefix
        sequential += np.trace(A @ rho[j] @ A.T) / M
        prefix = (H-P[j]) @ prefix
    assert pgm + 1e-9 >= C/(C+M-1)
    assert pgm <= min(1,C/M)+1e-9
    assert sequential+1e-9 >= 1-2*(M-1)/C
    return dict(d=d,M=M,m=m,t=t,C=C,lower=C/(C+M-1),pgm=float(pgm),upper=min(1,C/M),sequential=float(sequential),gram_moments=[float(a) for a in moments],nuclear_success_upper=float(nuclear_success_upper),error_lower=error_lower,optimal_binary=optimal_binary)


def check_clean_reflection(d=2,K=3):
    ps = list(permutations(range(K)))
    N = len(ps)
    D = d**K
    u = np.ones(N)/np.sqrt(N)
    e0 = np.eye(N)[0]
    v=e0-u
    prep=np.eye(N)-2*np.outer(v,v)/np.dot(v,v)
    select = np.zeros((N*D,N*D))
    for j,p in enumerate(ps):
        select[j*D:(j+1)*D,j*D:(j+1)*D] = perm_matrix(d,K,p)
    A=np.kron(prep,np.eye(D))
    W=A.T@select@A
    R0=np.kron(2*np.outer(e0,e0)-np.eye(N),np.eye(D))
    reflected=W.T@R0@W
    P=sum(perm_matrix(d,K,p) for p in ps)/N
    assert np.linalg.norm(reflected[:D,:D]-(2*P-np.eye(D)))<1e-9
    assert np.linalg.norm(reflected[D:,:D])<1e-9
    return dict(d=d,K=K,clean_reflection_error=float(np.linalg.norm(reflected[:D,:D]-(2*P-np.eye(D)))),leakage=float(np.linalg.norm(reflected[D:,:D])))


if __name__ == '__main__':
    rng=np.random.default_rng(20261101)
    cases=[(2,2,1,1),(2,3,1,1),(2,4,1,1),(2,2,2,1),
           (2,3,2,1),(2,2,1,3),(3,2,1,2),(3,3,1,1),
           (1,4,2,3),(2,3,0,1),(2,3,1,0),(2,1,1,1)]
    results={'matrix_cases':[check(*c) for c in cases],
             'clean_reflection':check_clean_reflection(),
             'posterior_checks':[posterior_checks(*c,rng) for c in [(2,1,2,3),(2,2,2,3),(3,1,2,3)]],
             'revealed_query_endpoint':[revealed_endpoint(Dm,M) for Dm,M in [(1,4),(2,3),(3,4),(6,3),(3,1)]],
             'complex_fixed_library':[fixed_library_checks(2,m,t,rng) for m,t in [(1,1),(1,3),(2,2),(3,2)]],
             'haar_quadrature_posteriors':haar_quadrature_checks(rng),
             'finite_covariant_checks':finite_covariant_checks(),
             'covariant_asymptotics':[covariant_asymptotic(a,round(a*a),m) for m in (1,2,3) for a in (10,30,100,300)],
             'scope':'Finite matrix identities and deterministic attaining-strategy quadrature; no numerical proof of universal claims or novelty.'}
    print(json.dumps(results,indent=2))
