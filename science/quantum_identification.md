# Quantum identification from supplied references

The task is to identify one member of an unknown quantum reference collection. There are $`M\geq1`$ labels and independent Haar pure states $`\psi_1,\ldots,\psi_M`$ in $`\mathbb C^d`$. The input contains $`m`$ copies of each labeled reference and $`t`$ query copies of $`\psi_J`$, with $`J`$ uniform on $`\{1,\ldots,M\}`$. Here $`d\geq1`$ and $`m,t\geq0`$ are integers. A discriminator receives these physical states, without their classical descriptions or preparation oracles, and outputs one label. It may use any joint measurement. The optimum below is the Bayesian optimum, averaged over both the independent Haar library and the uniform label.

Write

```math
D_s=\binom{d+s-1}{s},\qquad
C=\frac{D_mD_t}{D_{m+t}}.
```
The dimension $`D_s`$ is that of $`\mathrm{Sym}^s(\mathbb C^d)`$, with $`D_0=1`$. Let $`P_{\mathrm{opt}}`$ be the optimal success probability and $`e_{\mathrm{opt}}=1-P_{\mathrm{opt}}`$.

## Finite-dimensional bounds

For every $`M\geq2`$,

```math
\frac{C}{C+M-1}
\leq P_{\mathrm{opt}}
\leq \min\!\left\{1,\frac CM\right\},
```
and

```math
\max\!\left\{0,1-\frac CM,
\frac{M-1}{8C+4(M-2)}\right\}
\leq e_{\mathrm{opt}}
\leq \frac{M-1}{C+M-1}.
```
A sequential algorithm using true projective symmetry measurements satisfies

```math
e_{\mathrm{seq}}\leq
\min\!\left\{1,\frac{2(M-1)}C\right\}.
```
Thus $`P_{\mathrm{opt}}=\Theta(\min\{1,C/M\})`$ and $`e_{\mathrm{opt}}=\Theta(\min\{1,(M-1)/C\})`$, with absolute constants. The two order statements describe different parts of the same tradeoff: success when identification is difficult, and error when it is reliable. Neither asserts an exact formula for the finite-query optimum.

For $`0\lt\epsilon\leq1/8`$, error at most $`\epsilon`$ requires

```math
C\geq\frac{M-1}{16\epsilon},
```
whereas the sequential algorithm attains that error whenever $`C\geq2(M-1)/\epsilon`$. If the necessary lower bound exceeds the available maximum of $`C`$, the requested error is impossible with that reference budget. Failing the sufficient scan condition alone does not prove impossibility.

When $`M=1`$, the error is zero. When $`d=1`$, $`m=0`$, or $`t=0`$, the label carries no observable information and $`P_{\mathrm{opt}}=1/M`$ exactly. The displayed general bounds remain valid but need not be tight in their constants.

## Haar averaging gives flat projector hypotheses

Use the support space

```math
\mathcal H=
\left(\mathrm{Sym}^{m}\mathbb C^d\right)^{\otimes M}
\otimes\mathrm{Sym}^{t}\mathbb C^d,
\qquad L=\dim\mathcal H=D_m^MD_t.
```
Let $`P_j`$ be the orthogonal projector that symmetrizes the query registers jointly with reference block $`j`$, and acts as the identity on the other reference blocks. The restriction to $`\mathcal H`$ is well defined: a state symmetric on the combined block is separately symmetric on either subblock. Every $`P_j`$ has rank

```math
r=D_{m+t}D_m^{M-1}=\frac LC.
```
The Haar moment identity

```math
\int\psi^{\otimes s}\,d\psi
=\frac{\Pi_s}{D_s}
```
and independence of the other references give the averaged hypotheses

```math
\rho_j=\frac{P_j}{r}.
```
This reduction includes adaptive protocols and intermediate measurements: any such protocol is a final POVM on its initial supplied systems. It does not replace a correlated or known reference collection by the independent Haar model.

The null state $`\rho_0=I_{\mathcal H}/L`$ obeys $`\rho_j\leq C\rho_0`$. Therefore every POVM $`\{E_j\}_{j=1}^M`$ satisfies

```math
P_{\mathrm{success}}
=\frac1M\sum_j\mathrm{Tr}(E_j\rho_j)
\leq\frac CM\sum_j\mathrm{Tr}(E_j\rho_0)
=\frac CM.
```
This proves the success converse without computational or measurement-locality assumptions.

## Exact pair and triple overlaps

Suppressing identity factors on the other reference blocks, the partial trace over the private reference block $`R_j`$ is

```math
\mathrm{Tr}_{R_j}P_j
=\frac{D_{m+t}}{D_t}I_T
=\frac{D_m}{C}I_T.
```
Unitary covariance makes this partial trace a scalar on the irreducible query space $`\mathrm{Sym}^t\mathbb C^d`$, and the full trace fixes the scalar. Tracing a label that occurs only once in a product then gives

```math
\mathrm{Tr}(P_iP_j)=\frac rC
\quad(i\neq j),\qquad
\mathrm{Tr}(P_iP_jP_k)=\frac r{C^2}
\quad(i,j,k\text{ distinct}).
```
The second formula does not assume commuting projectors. The block traced at each step belongs to only one projector, so operators on all remaining blocks can be taken outside that partial trace.

Put $`S=\sum_jP_j`$, $`\beta=(M-1)/C`$, and $`\gamma=(M-1)(M-2)/C^2`$. Expansion of the powers, with cyclicity of trace and $`P_j^2=P_j`$, gives

```math
\begin{aligned}
\mathrm{Tr}S&=Mr,\\
\mathrm{Tr}S^2&=Mr(1+\beta),\\
\mathrm{Tr}S^3&=Mr(1+3\beta+\gamma).
\end{aligned}
```
## Pretty-good measurement

On $`\mathrm{supp}S`$, define

```math
E_j=S^{-1/2}P_jS^{-1/2}.
```
The inverse is the support inverse. The orthogonal complement has zero probability under every hypothesis and can be assigned to any label.

For a fixed label,

```math
\mathrm{Tr}(P_jS)
=r\left(1+\frac{M-1}{C}\right).
```
Apply scalar Jensen to the spectral distribution of $`S`$ under the positive normalized functional $`X\mapsto\mathrm{Tr}(P_jX)/r`$. Since $`x^{-1/2}`$ is convex on positive numbers,

```math
\mathrm{Tr}(P_jS^{-1/2})
\geq\frac{r}{\sqrt{1+(M-1)/C}}.
```
For $`X_j=P_jS^{-1/2}P_j`$, Cauchy–Schwarz on its rank $`r`$ support gives

```math
\mathrm{Tr}(X_j^2)
\geq\frac{[\mathrm{Tr}X_j]^2}{r}
\geq\frac{r}{1+(M-1)/C}.
```
As $`\mathrm{Tr}(E_j\rho_j)=\mathrm{Tr}(X_j^2)/r`$, averaging proves $`P_{\mathrm{opt}}\geq C/(C+M-1)`$. This measurement establishes the information bound; its global inverse square root is not used as an efficient implementation claim.

## Sequential symmetry decoder

Test $`\{P_j,I-P_j\}`$ in a fixed label order, stopping at the first acceptance. If every test rejects, output any label. Under hypothesis $`j`$, consider the outcome sequence that rejects labels $`1,\ldots,j-1`$ and accepts $`j`$. The correct projector has initial rejection probability zero, and every earlier incorrect projector has initial acceptance probability $`1/C`$.

Gao's noncommutative union bound, with its factor four, therefore gives

```math
\Pr[\mathrm{error}\mid J=j]
\leq\frac{4(j-1)}C.
```
Averaging the uniformly distributed label proves $`e_{\mathrm{seq}}\leq2(M-1)/C`$, with the trivial cap at one. The union bound applies to the mixed averaged hypotheses by linearity or purification. It explicitly accounts for the disturbance caused by earlier rejections; independent-test reasoning would not justify this protocol.

An efficient algorithm also attains the success order in the difficult regime. If $`C\lt4`$, random guessing suffices up to a constant factor. Otherwise choose a uniformly random subset of

```math
\ell=\min\{M,\lfloor C/4\rfloor\}
```
labels and run the scan on that subset. Conditional on including the true label, the mean error is at most $`2(\ell-1)/C\leq1/2`$. This yields success at least $`\frac1{16}\min\{1,C/M\}`$, using at most $`\ell`$ comparisons. The full scan is the useful version for small target error.

## Error converse from three moments

The discrimination trace bound used here is the established generalized Holevo–Curlander bound, not a new inequality. Its specialized application can be proved directly.

Choose isometries $`V_j:\mathbb C^r\to\mathcal H`$ with $`V_jV_j^\dagger=P_j`$, concatenate them as $`T=[V_1\ \cdots\ V_M]`$, and let $`G=T^\dagger T`$ on an $`n=Mr`$ dimensional space. The nonzero spectra of $`G`$ and $`S=TT^\dagger`$ agree. The zero multiplicities of $`G`$ must be retained below.

For a POVM $`\{E_j\}`$ set $`B_j=V_j^\dagger E_jV_j`$, so $`0\leq B_j\leq I`$. Stack $`\sqrt{E_j}`$ into an isometry $`A:\mathcal H\to\bigoplus_j\mathcal H`$. In the polar decomposition $`\sqrt{E_j}V_j=W_j\sqrt{B_j}`$, each $`W_j`$ can be a contraction, and $`W=\bigoplus_jW_j`$ is also a contraction. Thus

```math
\sum_j\mathrm{Tr}\sqrt{B_j}
=\mathrm{Tr}(W^\dagger AT)
\leq\|T\|_1
=\mathrm{Tr}\sqrt G.
```
Since $`\mathrm{Tr}B_j\leq\mathrm{Tr}\sqrt{B_j}`$,

```math
P_{\mathrm{success}}
\leq\frac{\mathrm{Tr}\sqrt G}{n}.
```
Let $`\mathbb E`$ denote the empirical mean over all $`n`$ eigenvalues $`\lambda\geq0`$ of $`G`$. The exact moments above imply

```math
\mathbb E\lambda=1,\quad
\mathbb E(\lambda-1)^2=\beta,\quad
\mathbb E\bigl[\lambda(\lambda-1)^2\bigr]=\beta+\gamma.
```
Consequently

```math
e_{\mathrm{opt}}
\geq1-\mathbb E\sqrt\lambda
=\frac12\mathbb E(\sqrt\lambda-1)^2.
```
Cauchy–Schwarz and $`(\sqrt\lambda+1)^2\leq2(\lambda+1)`$ give

```math
\begin{aligned}
\beta^2
&\leq
\mathbb E(\sqrt\lambda-1)^2\,
\mathbb E\bigl[(\lambda-1)^2(\sqrt\lambda+1)^2\bigr]\\
&\leq2(2\beta+\gamma)\,
\mathbb E(\sqrt\lambda-1)^2.
\end{aligned}
```
For $`M\geq2`$, $`\beta>0`$. Substitution yields

```math
e_{\mathrm{opt}}
\geq\frac{\beta^2}{4(2\beta+\gamma)}
=\frac{M-1}{8C+4(M-2)}.
```
Pair overlaps alone would not establish this error accumulation: different subspaces could all share one small ambiguous component. The exact third moment controls that obstruction for this ensemble.

The exactly revealed-query optimum has its proof in the [endpoint account](revealed_query.md). Dimension-dependent regimes are collected in [interpretation](interpretation.md).

## Fixed and typical libraries

Write $`B=\binom{m+t}{m}`$. For a deterministic library set $`x_{ij}=|\langle\psi_i|\psi_j\rangle|^2`$. A false comparison has exact acceptance

```math
F_{m,t}(x)=
\frac{\displaystyle\sum_{a=0}^{\min(m,t)}
\binom ma\binom ta x^a}{\binom{m+t}{m}}.
```
To see this, average all permutations of the $`m+t`$ systems and group them by the number $`a`$ of positions transferred across each of the two constant-state blocks. There are $`m!t!\binom ma\binom ta`$ such permutations, and their product-state expectation is $`x^a`$. Vandermonde's identity verifies $`F_{m,t}(1)=1`$.

The same sequential algorithm, with the same fixed operations, obeys the deterministic mean-error bound

```math
e_{\mathrm{seq}}(\text{library})
\leq\frac4M\sum_{i<j}F_{m,t}(x_{ij}).
```
If every overlap is at most $`\delta`$, then $`F_{m,t}(x)\leq e^{mt\delta}/B`$, so the mean error is at most $`2(M-1)e^{mt\delta}/B`$; the worst per-label error is at most twice that value. These are sufficient library conditions, without a pointwise converse.

For $`d\geq2`$, independent Haar pairs satisfy $`\Pr[x_{ij}>\delta]=(1-\delta)^{d-1}\leq e^{-(d-1)\delta}`$. A union bound gives maximum overlap at most

```math
\delta=\frac{2\log M+\log(1/\eta)}{d-1}
```
with probability at least $`1-\eta`$ whenever the displayed $`\delta\leq1`$. If $`d-1\geq mt[2\log M+\log(1/\eta)]`$, the false-comparison factor $`e^{mt\delta}`$ is at most $`e`$.

The Bayesian converse must not be promoted to an all-library converse. For any fixed universal discriminator, Markov's inequality gives $`\Pr_{\mathrm{library}}[P_{\mathrm{success}}\geq s]\leq C/(Ms)`$ for $`s>0`$. A conditioning event $`E`$ of positive Haar probability has conditional mean success at most $`C/[M\Pr(E)]`$. These are precisely the available typical-library and promise-family consequences.

## Attribution and verification

Haar integration, binary programmable identification, pretty-good measurements, Gao’s factor-four union bound, and Tyson’s generalized Holevo–Curlander bound are inherited. See [related work](../references/RELATED_WORK.md) for exact sources and the surviving multiclass contribution. [Verification](../verification/README.md) supplements these general proofs with finite projector, decoder and endpoint checks.
