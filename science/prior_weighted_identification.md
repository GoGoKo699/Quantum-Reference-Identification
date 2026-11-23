# Identification with unequal label priors

[Scientific account](README.md) · [Classical preprocessing](classical_preprocessing.md) · [Quantum identification](quantum_identification.md)

A known deployment prior can make the best classical-record decoder ignore its query altogether. The exact threshold is set by a binomial coefficient in the reference and query copy counts. A retained quantum reference can still improve the decision. More generally, a unique most probable label makes the retained optimum strictly better throughout the range of priors with at least two possible labels.

## Model and results

Draw $`M\geq2`$ independent Haar pure states in dimension $`d\geq2`$, with $`m\geq1`$ labeled reference copies of each. A single query consists of $`t\geq1`$ copies of reference $`J`$. The known probabilities $`\pi_1\geq\pi_2\geq\cdots\geq\pi_M`$ sum to one and are independent of reference preparation. All $`Mm+t`$ specimens are supplied and charged. In the classical training interface, an arbitrary collective measurement of the references leaves only a classical record before query arrival. The later query POVM may depend on that record. The retained interface permits an arbitrary joint reference-query POVM.

Write $`D_s=\binom{d+s-1}{s}`$, $`B=\binom{m+t}{m}`$, and $`C=D_mD_t/D_{m+t}`$. Let $`R_{\rm C}`$ and $`R_{\rm Q}`$ be the optimal average errors under zero-one loss in the two interfaces. The following statements hold for finite copy counts.

1. **Most probable label rule.** $`R_{\rm C}=1-\pi_1`$ if and only if $`\pi_1\geq B\pi_2`$. Under strict inequality, every optimal decision guesses label 1 with probability one. At equality, some other decisions can tie the optimum.
2. **A retained reference.** Testing joint symmetry with the most probable reference alone and guessing label 2 on rejection yields risk $`1-\pi_1-\pi_2(1-1/C)`$. This strictly improves on the most probable label rule if $`\pi_2\gt0`$.
3. **A unique most probable label.** If $`\pi_1\gt\pi_2\gt0`$, then $`R_{\rm Q}\lt R_{\rm C}`$, including when the classical record already improves on the most probable label rule.

For $`M=d=2`$ and $`t=1`$, setting $`m=n`$ and $`\pi_2=q`$ gives the threshold $`q\leq1/(n+2)`$ and the finite-training activation theorem in [Quantum Learning Class Imbalance](https://github.com/GoGoKo699/Quantum-Learning-Class-Imbalance). That project supplies the exact balanced-qubit comparator and develops the [binary rarity sample law](https://github.com/GoGoKo699/Quantum-Learning-Class-Imbalance/blob/main/science/rare_class_query_copies.md).

## Exact posterior bounds for a classical record

Let $`E_y`$ be a training POVM effect on $`(\mathrm{Sym}^m(\mathbb C^d))^{\otimes M}`$. The average training state is the normalized identity, so the training outcome law is independent of the query label. For $`\mathrm{Tr}E_y\gt0`$, the one-label training density operator is

```math
a_{y,j}=\frac{\mathrm{Tr}_{\ne j}E_y}{\mathrm{Tr}E_y}.
```

This representation permits collective measurements across all reference blocks. The Haar moment identity gives the conditional query state in the form

```math
\sigma_{y,j}
=D_m\int\!\langle\psi^{\otimes m}|a_{y,j}|\psi^{\otimes m}\rangle
\, (|\psi\rangle\langle\psi|)^{\otimes t}\,d\psi
=\frac{D_m}{D_{m+t}}\mathrm{Tr}_m[(a_{y,j}\otimes I)\Pi_{m+t}],
```

where $`\Pi_s`$ projects onto the symmetric subspace of $`s`$ systems. These formulas apply to effect densities almost everywhere for a continuous classical record.

The state-independent term of the [universal estimation-channel decomposition](classical_preprocessing.md#the-inherited-finite-query-common-component) is $`I_{\mathrm{Sym}^t}/B`$ in the partial-trace expression. The other terms are positive because they compress operators built from reduced states of $`a_{y,j}`$. This gives the lower bound below. The positive map $`X\mapsto\mathrm{Tr}_m[(a_{y,j}\otimes I)X]`$ applied to $`\Pi_{m+t}\preceq I`$ gives the upper bound.

```math
\frac{D_m}{B D_{m+t}}I_{\mathrm{Sym}^t}
\preceq\sigma_{y,j}
\preceq\frac{D_m}{D_{m+t}}I_{\mathrm{Sym}^t}.
```

The endpoints are attained against $`v^{\otimes t}`$ for a unit vector $`v`$. The upper endpoint uses $`a_{y,j}=|v^{\otimes m}\rangle\langle v^{\otimes m}|`$. The lower endpoint uses $`a_{y,j}=|u^{\otimes m}\rangle\langle u^{\otimes m}|`$ with $`\langle u|v\rangle=0`$. The squared norm of the symmetrized product $`u^{\otimes m}\otimes v^{\otimes t}`$ is $`1/B`$. Exactly $`m!t!`$ of the $`(m+t)!`$ permutations preserve both orthogonal blocks.

When $`\pi_1\geq B\pi_2`$, the bounds imply $`\pi_1\sigma_{y,1}\succeq \pi_j\sigma_{y,j}`$ for every $`j`$. Summing against the positive query POVM effects and using completeness bounds conditional success by $`\pi_1`$. Strict inequality gives positive definite dominance, so any nonzero effect for another label loses success on that record.

For the converse, a projective training measurement can include the product effect $`|u^{\otimes m}\rangle\langle u^{\otimes m}|`$ on reference 1 and $`|v^{\otimes m}\rangle\langle v^{\otimes m}|`$ on reference 2, with identity on the remaining references. It occurs with probability $`D_m^{-2}`$. On this outcome, guess label 2 if the query projector onto $`v^{\otimes t}`$ clicks, and otherwise guess label 1. On every other training outcome guess label 1. The gain in total success is exactly

```math
\frac{1}{D_m D_{m+t}}\left(\pi_2-\frac{\pi_1}{B}\right).
```

This gain is positive when $`\pi_1\lt B\pi_2`$ and zero when $`\pi_1=B\pi_2`$. At equality the event leading to a label-2 decision has positive probability.

## A one-reference quantum decision

Perform the projective symmetry test on reference 1 and the query. The correct reference always passes when $`J=1`$. An independent Haar reference has mean acceptance $`1/C`$ under any other label, since the pair's average state is the normalized identity on $`\mathrm{Sym}^m\otimes\mathrm{Sym}^t`$. Guess label 1 on acceptance and label 2 on rejection. The success is $`\pi_1+\pi_2(1-1/C)`$, with $`C\gt1`$ in the stated parameter range. This protocol retains only the most probable reference, performs one comparison, and can consume the tested specimens.

## Why a classical record loses with a unique most probable label

The Haar-averaged hypotheses are $`P_j/r`$, where $`P_j`$ jointly symmetrizes reference $`j`$ and the query, acts as identity on the other reference blocks, and has common rank $`r=D_m^{M-1}D_{m+t}`$. Fix two orthonormal local levels $`|0\rangle,|1\rangle`$. All hypotheses preserve the state $`|\Omega\rangle=|0\rangle^{\otimes(Mm+t)}`$ and the subspace $`W`$ with exactly one $`|1\rangle`$ and all other specimens in $`|0\rangle`$. In the symmetric block support, a basis of $`W`$ consists of the normalized symmetric excitation in each reference $`|R_k\rangle`$ or in the query $`|T\rangle`$.

Let $`F_j`$ denote the full decision POVM effects. A classical training strategy gives

```math
F_j=\int E_y\otimes Q_{j|y}\,dy,
```

where $`Q_{j|y}`$ is the conditional query POVM. Thus each effect is positive under partial transposition on the query. On $`|\Omega\rangle`$, all $`P_j`$ act as identity. A globally optimal decision therefore has $`\langle\Omega|F_j|\Omega\rangle=0`$ for $`j\ne1`$ because the prior's maximum is unique. Changing the POVM on that invariant line alone would improve any other assignment.

If $`F_j^{T_T}\succeq0`$ for $`j\ne1`$, its diagonal entry at $`\Omega`$ is also zero, so its entire row there vanishes. Choose the query transpose basis to include its all-zero state and its normalized symmetric excitation. The row at $`\Omega`$, evaluated on the state with one excitation in reference $`k`$ and one in the query, gives

```math
\langle T|F_j|R_k\rangle=0.
```

Completeness gives the same identities for $`F_1`$.

Set $`a=m/(m+t)`$ and $`b=t/(m+t)`$. On $`W`$, $`P_j`$ fixes $`|R_k\rangle`$ for $`k\ne j`$, and acts as the projector onto $`\sqrt a|R_j\rangle+\sqrt b|T\rangle`$ on the two remaining basis states. The possible off-diagonal contributions all connect a reference to the query. If those matrix elements vanish in every effect, the best success on $`W`$ makes the following assignments.

- On $`|T\rangle`$ and $`|R_k\rangle`$ with $`k\ne1`$, guess label 1.
- On $`|R_1\rangle`$, choose the larger of $`a\pi_1`$ and $`\pi_2`$.

Hold all other basis decisions fixed and allow a joint decision between labels 1 and 2 on the subspace spanned by $`|R_1\rangle,|T\rangle`$. The unnormalized weighted difference there is

```math
H=
\begin{pmatrix}
a\pi_1-\pi_2 & \sqrt{ab}\,\pi_1\\
\sqrt{ab}\,\pi_1 & b(\pi_1-\pi_2)
\end{pmatrix},
\qquad
\det H=-b\pi_2\big[(1+a)\pi_1-\pi_2\big]\lt0.
```

The opposite-sign eigenvalues make the positive spectral projector the unique optimizing effect for label 1 in this binary block. Its off-diagonal entry is nonzero. This change therefore strictly exceeds the best diagonal success on $`W`$. Since $`W`$ is invariant under every hypothesis, a new POVM on $`W`$ may be combined with the old effects compressed to the orthogonal complement of $`W`$. No globally optimal POVM can be PPT across the reference-query cut. The finite-dimensional set of such PPT POVMs is compact, so even its best success is strictly below the global optimum.

## Example and scope

For $`d=2,m=1,t=2`$, $`B=3`$ and $`C=3/2`$. With prior $`(0.75,0.20,0.05)`$, classical training has error $`0.25`$, and retaining the first reference gives error $`0.25-0.20/3\approx0.1833`$. With prior $`(0.60,0.30,0.10)`$, classical training already helps, and the unique-maximum theorem still guarantees a strictly lower retained optimum.

The result concerns one finite query with independent Haar pure references and known priors. The exact classical threshold includes ties. The strict-gap proof assumes a unique largest prior and a positive second-largest prior. It leaves the retained-versus-classical comparison with tied largest priors to separate arguments, including the existing balanced single-query-qubit equality and the [large uniform library result](interpretation.md). If only one label has positive prior, its risk is zero without either resource. With zero reference or query copies, or with dimension one, the two interfaces both achieve $`1-\pi_1`$.

## Attribution

[Chiribella (2010), Eqs. (6)–(7)](https://arxiv.org/abs/1010.1875v4) supplies the positive decomposition of the universal estimation channel. [Anshu, Landau and Liu (2022)](https://doi.org/10.1145/3519935.3519974) use its shared posterior component in distributed inner-product estimation. The exact prior threshold uses that component, a matching upper eigenvalue bound, and a decision that attains both endpoints on one classical outcome.

The symmetry comparison and the binary retained optimum have prior accounts, including [He and Bergou (2007)](https://doi.org/10.1103/PhysRevA.75.032316) and [Zhou et al. (2012)](https://www.rintonpress.com/xxqic12/12-11-12/1017-1033.pdf). [Sentís et al. (2012)](https://doi.org/10.1038/srep00708) establish the balanced memory-free qubit result. [Quantum Learning Class Imbalance's one-excitation argument](https://github.com/GoGoKo699/Quantum-Learning-Class-Imbalance/blob/227c936950dd075860d8bfa15d5009a1c6b11d42/science/activation.md) supplies the PPT mechanism that extends here to any finite query width, dimension, and number of classes with a unique top prior.
