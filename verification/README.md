# Reproducing the finite checks

Run from the repository root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 verification/check_reference_identification.py > verification/results.new.json
```

The script requires Python 3, NumPy and SciPy. It uses the fixed seed `20261101`
for the posterior examples. All assertions pass in the recorded run using
Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0.

The 12 dense matrix configurations include one, two, three and four labels;
qubits and qutrits; several positive copy counts; and the indistinguishable
edge cases `d=1`, `m=0` and `t=0`. For each configuration the script constructs
the averaged hypotheses from permutation projectors and checks the ranks,
every ordered pair and triple trace, all three normalized Gram moments,
the pretty-good measurement, the sequential decoder, the capacity ceiling
and the explicit error floor. The binary cases also check the exact
Helstrom optimum. These finite checks do not compute the multiclass optimum.

An independent occupation-basis construction checks the posterior moment
converse and the inherited finite-query common component. The examples
include reduced states of entangled collective training effects. Independent
Haar quadrature checks three such qubit posteriors, moments through order
six, and saturation of every tested moment by a coherent posterior. Five
commuting discrimination examples evaluate the revealed-query retained-reference
endpoint in exact rational arithmetic. Four complex fixed-library examples
check the symmetric-projector acceptance polynomial. A permutation LCU
matrix checks the clean symmetric-subspace reflection and its zero
work-register leakage.

Finally, deterministic quadrature evaluates the exact covariant-training
attaining strategy for fixed `m=1,2,3`, with `log M=10,30,100,300` and
`d=(log M)^2`. Its ratio to `(log M)^m/m!` after multiplication by `M`
approaches one. The optimized finite-dimensional moment converse is checked
above the attaining value. This is a numerical illustration of the
asymptotic theorem, whose proof is separate. Six additional finite cases check
the attaining strategy below the moment converse; the four one-copy cases
also compare quadrature against the exact gamma-function expression.

Small negative eigenvalues around `1e-17` in `results.json` are floating-point
roundoff. Assertions use explicit numerical tolerances. A passed finite check
is neither a proof of an arbitrary-parameter statement nor a novelty review.

The checked dependency versions are pinned in [requirements.txt](requirements.txt). The saved [results.json](results.json) records the reproducible reference run; `results.new.json` is an optional fresh output for comparison.
