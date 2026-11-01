# Model and notation

## A delayed membership query

Let $`d,M\ge1`$ and $`m,t\ge0`$ be integers. Independently sample normalized pure states $`\psi_1,\ldots,\psi_M`$ from Haar measure on $`\mathbb C^d`$. A reference block $`R_j`$ contains $`m`$ copies of $`\psi_j`$. A label $`J`$ is uniform on $`\{1,\ldots,M\}`$ and independent of library preparation; the query block $`T`$ contains $`t`$ copies of $`\psi_J`$. The task is to return $`J`$ once. Success is averaged over the library, label and measurement outcomes.

The notation $`\psi`$ also denotes the rank-one density operator of a pure state. All measurements may depend on known parameters $`d,M,m,t`$. The state descriptions themselves are unknown. There is no preparation oracle, inverse oracle, source reflection, classical loading oracle or QRAM.

In the **retained-quantum model**, the reference blocks remain available when the query arrives. An arbitrary joint POVM is allowed, including adaptive processing and ancillas. The algorithm in [resources](resources.md) constructs a particular sequential measurement; an information-theoretic optimum does not imply an efficient implementation of every optimal POVM.

In the **classical-training model**, an arbitrary collective POVM acts on all references before any query information arrives. Its outcome may use unlimited classical information and computation. Every quantum system correlated with training is discarded across this boundary; retained entanglement or quantum side information would change the model. The later decoder can process the query with fresh ancillas and the classical record. A classical record is not restricted to separate per-reference estimates.

The **revealed-query comparison** gives the decoder the exact classical description of the later query state after training. This is extra information, so its classical-training success upper-bounds every finite $`t`$ classical-training protocol. It does not give reference descriptions. The [retained-quantum endpoint](revealed_query.md) uses the same later description while retaining physical reference blocks.

## Symmetric spaces

Define

```math
\mathcal S_s=\mathrm{Sym}^s(\mathbb C^d),\qquad
D_s=\dim\mathcal S_s=\binom{d+s-1}{s},\qquad
\tau_s=I_{\mathcal S_s}/D_s.
```
Use $`D_0=1`$. The normalized Haar moment is

```math
\int\psi^{\otimes s}\,d\psi=\tau_s.
```
The finite-query capacity parameter and permutation coefficient are

```math
C(d,m,t)=\frac{D_mD_t}{D_{m+t}},\qquad
B(m,t)=\binom{m+t}{m}.
```
All logarithms are natural unless marked $`\log_2`$. The error $`e_{\mathrm{opt}}`$ is one minus the supremal Bayesian success in the retained-quantum model. $`P_{\mathrm{classical}}^{\mathrm{revealed}}`$ is the supremal success over all classical-training protocols with the later exact query description.

For $`M=1`$, success is one. For $`d=1`$, $`m=0`$, or $`t=0`$ in the finite-query model, the hypotheses coincide and success is $`1/M`$. The sharp classical asymptotic holds for a **fixed positive** $`m`$ with $`M\to\infty`$ and $`d/\log M\to\infty`$; it makes no growing $`m`$ claim.

## Resource convention

Every input specimen is charged: $`Mm`$ reference copies and $`t`$ query copies. Keeping the library is a quantum memory resource. Its preparation costs are external source costs, not free algorithmic access. The explicit decoder charges its scan, work registers, known-wire swaps, classical bookkeeping, and rotation precision. A known-description comparator is an information benchmark with its own description input and measurement synthesis costs. No algorithm is asserted to return an undisturbed reusable library.
