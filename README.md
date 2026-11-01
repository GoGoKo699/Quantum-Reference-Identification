# Quantum Reference Identification

How much of a quantum reference library survives measurement before a future query is known? This project studies identification from supplied copies: retain the references as quantum states, or measure the entire library first and keep an unrestricted classical record.

A library contains $M$ independent Haar-distributed pure states in dimension $d$. The input consists of $m$ labeled copies of every reference and $t$ copies of a uniformly selected library member. The output is its label. No classical reference descriptions, preparation or inverse oracles, or QRAM are supplied.

Write

$$
D_s=\binom{d+s-1}{s},\qquad C=\frac{D_mD_t}{D_{m+t}}.
$$

For $M\ge 2$, the optimal average error obeys

$$
\frac{M-1}{8C+4(M-2)}\le e_{\mathrm{opt}}\le\frac{M-1}{C+M-1}.
$$

Sequential symmetric-subspace tests give an explicit decoder with error at most $2(M-1)/C$. Reliable identification therefore requires and permits $C$ of order $M/\epsilon$ for small target error $\epsilon$, up to universal constants.

The classical comparison allows **any collective measurement of all references**, unlimited computation and classical storage, but no quantum information from training may survive until the query arrives. Even revealing the exact later query state does not remove the fixed-reference ceiling. For each fixed positive integer $m$, as $M\to\infty$ and $d/\log M\to\infty$,

$$
P_{\mathrm{classical}}^{\mathrm{revealed}}
=(1+o(1))\frac{(\log M)^m}{m!M}.
$$

The logarithm is natural. The ceiling is attained to leading order by independent covariant reference measurements; its converse includes collective training. These statements quantify loss across a delayed-query memory boundary, with a fixed supplied reference budget.

| Question | Authoritative account |
|---|---|
| What is supplied, and when may it be measured? | [Model and notation](science/model.md) |
| What can retained quantum references accomplish? | [Finite-query identification](science/quantum_identification.md) |
| What survives classical preprocessing? | [Classical-record ceiling](science/classical_preprocessing.md) |
| What happens when the query is known exactly? | [Revealed-query endpoint](science/revealed_query.md) |
| How is the decoder implemented and charged? | [Implementation and resources](science/resources.md) |
| What is the operational consequence? | [Regimes and interpretation](science/interpretation.md) |
| Which ingredients and results are inherited? | [Related work](references/RELATED_WORK.md) |
| How can the finite identities be reproduced? | [Verification](verification/README.md) |

Start with the [connected science route](science/README.md). The [LLM reading guide](llms.txt) maps questions directly to proofs.

## Reproduce

```bash
python3 -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 verification/check_reference_identification.py
```

The verification guide states the tested instances, numerical tolerances and limits. Dense finite checks supplement the analytical proofs; they do not establish an unrestricted optimal measurement numerically.

## Scope

The results are Bayesian for an independent Haar pure-state library, a uniform label, equal reference-copy counts, and one lookup. They do not establish a worst-case arbitrary-library converse, mixed-state robustness, repeatable database use, or a total-runtime speedup. The decoder scans references, consumes real quantum storage, and charges all $Mm+t$ supplied specimens. Classical shadows already provide a logarithmic reference-copy comparator for a later known query; the fixed-$m$ success separation is not an exponential reference-sample advantage.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
