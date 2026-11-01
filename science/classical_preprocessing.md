# Classical preprocessing before the query arrives

[Scientific account](README.md) · [Model](model.md) · [Quantum matching](quantum_identification.md) · [Resources](resources.md)

The chronology in this section is essential. A processor receives $m$ copies of each of $M$ independently Haar-distributed pure references in $\mathbb C^d$. It measures the **entire reference collection before learning the query**, retains an unrestricted classical record, and discards every quantum system carrying information from training. Later it receives $t$ copies of a uniformly selected reference and returns its label. The training measurement may be collective across all labels; its output length and computational cost are unrestricted. Retaining quantum side information across this boundary is outside this model.

Write $P_{\mathrm{cl}}(d,M,m,t)$ for its optimal Haar-average success. Let $P_{\mathrm{cl}}^{\mathrm{rev}}(d,M,m)$ denote the more generous endpoint in which the decoder receives an exact classical description of the later query state, after training has ended. Then

$$
P_{\mathrm{cl}}(d,M,m,t)\leq P_{\mathrm{cl}}^{\mathrm{rev}}(d,M,m).
$$

This endpoint supplies later query information for free solely to strengthen an impossibility result. It does not supply descriptions of the reference collection or let the revealed query control the earlier measurement.

For integers $s\geq0$, define

$$
D_s=\binom{d+s-1}{s},\qquad
\tau_s=\frac{I_{\operatorname{Sym}^s(\mathbb C^d)}}{D_s}.
$$

Unless stated otherwise, $d\geq2$, $M\geq2$, and $m\geq1$ are integers. The degenerate cases appear below.

## A collective training measurement still has positive one-label posteriors

Restrict each reference block to $\mathcal K=\operatorname{Sym}^m(\mathbb C^d)$. Consider a training POVM effect $E_y\geq0$ on $\mathcal K^{\otimes M}$. The prior record probability and its effective effect on label $j$ are

$$
p_y=\operatorname{Tr}(E_y\tau_m^{\otimes M}),\qquad
A_{y,j}=\operatorname{Tr}_{\ne j}
 \left[E_y\left(I_j\otimes\tau_m^{\otimes(M-1)}\right)\right].
$$

Because each $\tau_m$ is a scalar identity on its support, $A_{y,j}$ is positive and

$$
\operatorname{Tr}A_{y,j}=D_m p_y.
$$

For $p_y>0$, set $a_{y,j}=A_{y,j}/(D_m p_y)$. This is a density operator on $\mathcal K$. The selected label $J$ is independent of the training process, so it remains uniform after conditioning on $y$. Relative to normalized Haar measure, the conditional density of the query state under label $j$ is

$$
q_{y,j}(\psi)=D_m\langle\psi^{\otimes m}|a_{y,j}|\psi^{\otimes m}\rangle.
$$

It integrates to one by the Haar moment identity. The conditional query marginal, without conditioning on $j$, need not be Haar; its density is $M^{-1}\sum_jq_{y,j}$. Bayes' rule nevertheless gives the optimal revealed-query success conditional on the record as

$$
P_y^{\mathrm{rev}}=\frac1M\int\max_{j\leq M}q_{y,j}(\psi)\,d\psi.
$$

For a finite query, the conditional $t$-copy state is

$$
\sigma_{y,j,t}=D_m\int
 \langle\psi^{\otimes m}|a_{y,j}|\psi^{\otimes m}\rangle
 (|\psi\rangle\langle\psi|)^{\otimes t}\,d\psi.
$$

No factorization of the training POVM has been assumed. Correlations between posterior reference blocks do not enter this one-query decoding objective. Continuous-outcome measurements use an effect density relative to a dominating measure; the same derivation holds almost everywhere, with integrations replacing sums.

## Finite-dimensional revealed-query converse

For every positive integer $s$, the Haar moment formula and $0\leq\Pi_{ms}\leq I$ imply

$$
\begin{aligned}
\int q_{y,j}(\psi)^s\,d\psi
&=\frac{D_m^s}{D_{ms}}
 \operatorname{Tr}\left(a_{y,j}^{\otimes s}\Pi_{ms}\right)\\
&\leq\frac{D_m^s}{D_{ms}}.
\end{aligned}
$$

Here $a_{y,j}^{\otimes s}$ is positive with trace one, whether or not $a_{y,j}$ is pure or is itself a tensor power. Pointwise, $\max_jq_j\leq(\sum_jq_j^s)^{1/s}$. Integrating and using concavity of the $1/s$ power gives

$$
P_y^{\mathrm{rev}}
\leq M^{1/s-1}\frac{D_m}{D_{ms}^{1/s}}.
$$

The bound is independent of the record, so it also holds after averaging over an arbitrary collective training measurement. Consequently,

$$
\boxed{
P_{\mathrm{cl}}^{\mathrm{rev}}(d,M,m)
\leq\min\left\{1,\inf_{s\in\mathbb N_{\geq1}}
 M^{1/s-1}\frac{D_m}{D_{ms}^{1/s}}\right\}.}
$$

The separate bound $P_{\mathrm{cl}}^{\mathrm{rev}}\leq D_m/M$ follows from $q_{y,j}\leq D_m$; it is also the fixed-$d,m,M$ limit of the displayed expression as $s\to\infty$. The $s=1$ term is the trivial upper bound one. No finite value of $s$ or bounded record size is assumed in the theorem.

The proof uses standard Haar moments and a power-method bound on discrimination. Those tools and the postmeasurement-information framework are inherited; the evaluated multiclass law is the contribution assessed here. See [the source comparison](../references/RELATED_WORK.md).

## A classical strategy with an exact finite-dimensional success formula

Measure each reference block independently using the covariant POVM

$$
D_m|\phi^{\otimes m}\rangle\langle\phi^{\otimes m}|\,d\phi,
$$

and record the directions $\phi_1,\ldots,\phi_M$. The outcomes are unconditionally independent Haar directions. When the query $\psi$ is revealed, return a label maximizing $|\langle\phi_j|\psi\rangle|^2$; the exponent $m$ does not change its ordering.

For a fixed revealed $\psi$, the random variables $X_j=|\langle\phi_j|\psi\rangle|^2$ are independent $\operatorname{Beta}(1,d-1)$ variables. Averaging the maximum posterior likelihood therefore gives the exact achievable value

$$
\boxed{
P_{\mathrm{cov}}(d,M,m)
=\frac{D_m}{M}\mathbb E\left[\left(\max_{j\leq M}X_j\right)^m\right]
\leq P_{\mathrm{cl}}^{\mathrm{rev}}(d,M,m).}
$$

For $m\geq1$, an equivalent integral is

$$
\mathbb E\left[\left(\max_jX_j\right)^m\right]
=m\int_0^1x^{m-1}
 \left[1-\left(1-(1-x)^{d-1}\right)^M\right]dx.
$$

This is an exact formula for the specified protocol, **not** a claim of finite-parameter optimality among collective training measurements. In particular, when $m=1$ it simplifies to

$$
P_{\mathrm{cov}}(d,M,1)=\frac dM
\left[1-\frac{\Gamma(M+1)\Gamma(1+1/(d-1))}
 {\Gamma(M+1+1/(d-1))}\right].
$$

At fixed $M$ and $d\to\infty$, this tends to $H_M/M$, where $H_M=\sum_{j=1}^M1/j$. That limit concerns this protocol; it does not assert the exact finite-$M$ optimum.

## Sharp asymptotic ceiling for a fixed reference budget

**Theorem.** Fix a positive integer $m$. Along any sequence with $M\to\infty$ and $d/\log M\to\infty$,

$$
\boxed{
P_{\mathrm{cl}}^{\mathrm{rev}}(d,M,m)
=(1+o(1))\frac{(\log M)^m}{m!M}.}
$$

All logarithms are natural. The statement optimizes over arbitrary collective training measurements and unlimited classical records. Its quantifiers fix $m$; it is not a uniform theorem for growing $m$.

### Upper bound

Let $L=\log M$ and choose $s=\lfloor L/m\rfloor$, which is positive for all sufficiently large $M$. The elementary bounds

$$
D_m=\frac{(d)_m}{m!},\qquad
D_{ms}\geq\frac{d^{ms}}{(ms)!}
$$

give

$$
M P_{\mathrm{cl}}^{\mathrm{rev}}
\leq\frac{(d)_m}{d^m}
 \frac{M^{1/s}((ms)!)^{1/s}}{m!}.
$$

For fixed $m$, $(d)_m/d^m\to1$. Moreover, $s\sim L/m$ and $ms\sim L$. Stirling's formula gives

$$
\log\left(\frac{M^{1/s}((ms)!)^{1/s}}{L^m}\right)
=\frac Ls-m+m\log\frac{ms}{L}
 +O\left(\frac{\log(ms)}s\right)\longrightarrow0.
$$

This proves the required upper bound. In particular, no approximation of $D_{ms}$ by $d^{ms}/(ms)!$ with a vanishing relative error is needed. Requiring $d/(\log M)^2\to\infty$ for that unnecessary approximation would weaken the actual theorem.

### Attaining lower bound

Set $Y_j=-(d-1)\log(1-X_j)$. These variables are independent exponential variables of mean one. Their maximum $H=\max_jY_j$ obeys, for every fixed $0\lt\delta\lt1$,

$$
\Pr[H>(1+\delta)L]\leq M^{-\delta},\qquad
\Pr[H<(1-\delta)L]\leq e^{-M^\delta}.
$$

The same exponential tail bound, integrated above $L$, yields $\mathbb E H^m=(1+o(1))L^m$ for each fixed $m$. Let $Z=\max_jX_j=1-e^{-H/(d-1)}$. Since $Z\leq H/(d-1)$,

$$
\mathbb E Z^m\leq(1+o(1))\left(\frac Ld\right)^m.
$$

On the event $H\geq(1-\delta)L$,

$$
Z^m\geq\left(1-e^{-(1-\delta)L/(d-1)}\right)^m
=(1+o(1))\left(\frac{(1-\delta)L}{d}\right)^m,
$$

because $L/d\to0$. That event has probability tending to one. Taking the lower limit and then $\delta\downarrow0$ proves $\mathbb E Z^m=(1+o(1))(L/d)^m$. Finally $D_m=(1+o(1))d^m/m!$, so the exact covariant formula attains the upper bound.

## The inherited finite-query common component

For completeness, the finite-$t$ posterior channel has the universal measure-and-prepare decomposition studied by Chiribella. With $B=\binom{m+t}{m}$ and $C=D_mD_t/D_{m+t}$, the state-independent component has weight

$$
\alpha=\frac CB
=\prod_{a=0}^{m-1}\frac{d+a}{d+t+a}.
$$

In detail, for a density operator $a$ on $\operatorname{Sym}^m$, let $a^{(k)}$ be its $k$-register reduced state and $a^{(0)}=1$. The symmetric-projector identity reads

$$
\operatorname{Tr}_m[(a\otimes I)\Pi_{m+t}]
=\frac1B\sum_{k=0}^{\min(m,t)}
 \binom mk\binom tk\,
 \Pi_t(a^{(k)}\otimes I^{\otimes(t-k)})\Pi_t.
$$

Every term is positive. The $k=0$ term is $I_{\operatorname{Sym}^t}/B$, giving $\sigma_{y,j,t}\geq\alpha\tau_t$. The common component cannot carry the label, so

$$
P_{\mathrm{cl}}(d,M,m,t)
\leq1-\alpha+\frac\alpha M
\leq\frac1M+\frac{mt}{d}.
$$

The product formula should be used when the last relaxed bound exceeds one. The channel identity is inherited from [Chiribella, arXiv:1010.1875, Eqs. (6)–(7)](https://arxiv.org/abs/1010.1875); the posterior-common-component mechanism is used by [Anshu, Landau and Liu, arXiv:2111.03273, Lemma 7 and Theorem 9](https://arxiv.org/abs/2111.03273). Its many-label application is included for context and is not the main novelty claim. Unlike the revealed-query bound, this bound becomes uninformative as $t\to\infty$.

## Edge cases and scope

If $M=1$, success is one. If $d=1$ or $m=0$, the label cannot be distinguished and success is $1/M$, including at the revealed-query endpoint. If $t=0$, finite-query success is $1/M$. The beta-variable formula is stated for $d\geq2$; the $d=1$ case is handled separately.

At each fixed finite $d,M,m$, ordinary query-state tomography followed by the revealed-query decision rule approaches the endpoint as $t\to\infty$. The posterior likelihoods are continuous functions of a pure state on a compact space, so consistency of the tomography estimate makes the decision regret vanish; ties do not prevent convergence of the success value. This limiting statement grants no efficient tomography or finite-query implementation for free.

For fixed $m$ and a sufficiently large dimension, retained quantum references can achieve constant success with query copies of order $M^{1/m}$. The theorem above says that discarding those same references before the query arrives leaves success of order $(\log M)^m/M$ even with a perfect later query description. This is a statement about a fixed scarce-reference budget and irreversible preprocessing. It is not a computational speedup against an algorithm supplied classical descriptions of every reference, and it is not an exponential reference-sample advantage when the reference budget is allowed to grow. Classical-shadow protocols supply a known logarithmic-copy comparator in a separated-library revealed-query setting; [the source comparison](../references/RELATED_WORK.md) records that qualification.

## Verification

The [verification suite](../verification/README.md) checks finite covariant success, positive posterior operators from collective training effects, their Haar moments, the inherited common component, and the attaining-strategy asymptotic. These numerical checks support finite identities and arithmetic; the general and limiting statements follow from the analytical proofs above.
