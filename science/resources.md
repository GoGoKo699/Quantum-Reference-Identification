# Implementing and charging the symmetry scan

The sequential decoder uses at most $`M`$ true Lüders measurements of joint symmetry on the query block and one reference block. It needs no description of the unknown input states, no state-preparation or inverse oracle, and no QRAM. This page gives a conservative implementation bound, without claiming an optimal gate count or a faster database lookup.

Let $`K=m+t\geq2`$ and $`q=\lceil\log_2d\rceil`$. Encode each physical qudit in $`q`$ qubits. A permutation preserves the valid $`d`$-dimensional subspace of every register, so the embedding does not change the symmetry projector on the supplied inputs. The cases $`m=0`$, $`t=0`$, or $`d=1`$ require only random guessing.

## A clean reflection from permutation averaging

Let $`P`$ be the symmetric projector on the selected $`K`$ qudits. Its permutation-average form is

```math
P=\frac1{K!}\sum_{\pi\in S_K}U_\pi.
```
Prepare independent index registers uniformly on the known intervals $`\{0,\ldots,k-1\}`$ for $`k=2,\ldots,K`$. The associated Fisher–Yates swaps give a one-to-one encoding of all $`K!`$ permutations. Let $`V`$ be this known-state preparation and let $`U_{\mathrm{sel}}`$ apply the permutation specified by those registers. Invalid index encodings can be assigned arbitrary unitary actions, because their ideal prepared amplitudes vanish. With $`A=O(K\log K)`$ index qubits, define

```math
W=(V^\dagger\otimes I)U_{\mathrm{sel}}(V\otimes I),
\qquad
(\langle0|\otimes I)W(|0\rangle\otimes I)=P.
```
For $`u\in\mathrm{ran}P`$, all permutations fix $`u`$, so $`W(|0\rangle u)=|0\rangle u`$. For $`v\in\ker P`$, the zero-ancilla component of $`W(|0\rangle v)`$ vanishes. Thus, writing $`Z_0=2|0\rangle\langle0|-I`$,

```math
W^\dagger(Z_0\otimes I)W(|0\rangle v)
=|0\rangle(2P-I)v
```
for every data vector $`v`$. This implements the reflection $`R=2P-I`$ and returns all permutation workspace to zero in the ideal gate model.

Prepare an outcome flag in $`|+\rangle`$, control only the middle $`Z_0`$ on that flag, and apply the two surrounding $`W,W^\dagger`$ unconditionally. On the flag-zero branch those two unitaries cancel; on flag one they implement $`R`$. A final Hadamard and flag measurement have data Kraus operators

```math
\frac{I+R}{2}=P,\qquad
\frac{I-R}{2}=I-P.
```
The instrument is therefore the exact Lüders pair $`\rho\mapsto P\rho P`$ or $`\rho\mapsto(I-P)\rho(I-P)`$. Measuring the original permutation-average success flag alone would not establish the required rejection channel; the reflection construction supplies it.

## Gate count and precision

For each candidate Fisher–Yates index, compute an equality flag in $`O(\log k)`$ reversible gates, use it for $`q`$ controlled swaps between specified wires, and uncompute it. Summation over all candidate indices and steps gives $`O(K^2(q+\log K))`$ elementary reversible gates. Known interval-state preparation can be implemented by a direct binary-tree rotation construction using at most $`O(K^2\log K)`$ gates across all intervals. The reflection about the all-zero ancilla state needs $`O(A)`$ gates with clean scratch. Therefore one ideal comparison uses

```math
G=O\!\left(K^2(q+\log K)\right)
```
elementary gates, counting arbitrary one-qubit rotations, and $`O(K\log K)`$ ancillary qubits beyond the selected data registers. This is polynomial in the physical input size and in $`\log d`$; it is not a polynomial-in $`d`$ Schur-transform assumption.

For a finite gate set, choose each synthesized rotation to have operator error $`O(\delta/G)`$. Composition bounds then give operator error $`O(\delta)`$ for the comparison circuit and diamond-norm error $`O(\delta)`$ for its complete measurement instrument, including workspace reset. An adaptive hybrid argument over at most $`M`$ comparisons gives added statistical error $`O(M\delta)`$. Choosing $`\delta=\Theta(\eta/M)`$ makes this at most the specified $`\eta>0`$.

Using single-qubit Clifford+T approximation with $`O(\log(1/\zeta))`$ gate count for operator error $`\zeta`$, a conservative total scan count is

```math
O\!\left(
MG\log\frac{MG}{\eta}
\right),\qquad
G=O\!\left(K^2(q+\log K)\right).
```
Alternatively, a generic Solovay–Kitaev compiler gives the same polynomial resource statement with a polylogarithmic precision factor. The near-logarithmic rotation-synthesis count concerns circuit size; compiler classical runtime and its arithmetic assumptions should be charged if a concrete compiled implementation is requested. The supplied-copy result needs no uncharged computation on the unknown states.

The finite-gate circuit may leave a small residual workspace error. The diamond-instrument bound includes discarding and resetting that workspace; finite precision is not described as exact cleanup. With this synthesis choice, the actual success is at least $`1-2(M-1)/C-\eta`$, clipped at zero.

## Complete input and memory account

| Resource | Charged amount for the full scan |
| --- | --- |
| Supplied reference copies | $`Mm`$ unknown physical states |
| Supplied query copies | $`t`$ unknown physical states |
| Data storage when references precede query | $`(Mm+t)q`$ qubits |
| Additional circuit workspace | $`O(K\log K)`$ qubits |
| Active data per comparison | $`Kq`$ qubits |
| Comparisons | At most $`M`$ |
| Classical output | One label, requiring $`\lceil\log_2M\rceil`$ bits |
| Finite-gate scan | $`O(MG\log(MG/\eta))`$ gates under the stated synthesis convention |

All source-preparation or acquisition costs are additional charged costs for the $`Mm+t`$ supplied copies. The Haar model specifies an input distribution; it does not assert efficient preparation of arbitrary Haar states. The reference bank is physically retained until it is used or discarded, rather than supplied through a free addressing oracle. Controlled swaps connect known wires, and the label scan is classical control.

The same $`t`$ query copies are used across comparisons. Their disturbance is already included in the noncommutative union-bound analysis. This is a single-lookup theorem: later reuse of the references or queries is not guaranteed, and the protocol may consume or disturb both. A random-subset decoder can retain fewer references after an initial choice, but acquisition of the original $`Mm`$ supplied states is still charged.

For $`m=1`$ and $`t`$ proportional to $`M`$, the bound is polynomial but can scale as $`\widetilde O(M^3\log d)`$. The result establishes the number of supplied quantum specimens needed for identification and the possibility of a finite circuit. It does not establish a runtime advantage over a classical algorithm with fully described templates.

Primary synthesis reference: [Ross and Selinger, Optimal ancilla-free Clifford+T approximation of z-rotations](https://arxiv.org/abs/1403.2975). The quantum union bound is [Gao, Phys. Rev. A 92, 052331 (2015)](https://arxiv.org/abs/1410.5688). The clean-reflection derivation above is included explicitly so the instrument and its rejected branch can be checked without an oracle implementation assumption.
