# Regimes and interpretation

## Finite-query frontier

The [quantum identification bounds](quantum_identification.md) give a dimension-sensitive parameter $C=D_mD_t/D_{m+t}$. For $B=\binom{m+t}{m}$, its exact relation to the binomial coefficient is

$$
\frac{C}{B}=\prod_{a=0}^{m-1}\frac{d+a}{d+t+a},\qquad
e^{-mt/d}B\le C\le B.
$$

Thus $C\sim B$ when $mt/d\to0$. This approximation is not uniform when $t$ is comparable to $d$. For fixed positive $m$ and a dimension large enough relative to $mt$, constant-success identification has query scale $t=\Theta_m(M^{1/m})$. At small target error, use the exact $C=\Theta(M/\epsilon)$ criterion and its stated constants.

For one reference copy per class,

$$
C(d,1,t)=\frac{d(t+1)}{d+t}.
$$

As $t\to\infty$ at fixed $d,m$, $C\to D_m$. A scarce reference budget imposes a ceiling even if an arbitrarily large number of later queries is supplied. The [revealed-query endpoint](revealed_query.md) determines the retained-quantum optimum in that ideal-information comparison.

## What classical preprocessing loses

For each fixed $m\ge1$, arbitrary collective classical training has revealed-query success

$$
P_{\mathrm{classical}}^{\mathrm{revealed}}
=(1+o(1))\frac{(\log M)^m}{m!M},
\qquad M\to\infty,\quad d/\log M\to\infty.
$$

With $m=1$, take $t=aM$ for a sufficiently large constant $a$ and $d/M\to\infty$. The quantum scan has constant success, while every classical-training protocol has success at most $(1+o(1))\log M/M$ even if the later query is known exactly, and that ceiling is attained to leading order. Increasing later query information cannot recover the reference information discarded before the query was known.

For any fixed positive $m$, the same comparison uses $t$ of order $M^{1/m}$ with a sufficiently large constant and $d$ large enough for the capacity condition. The theorem compares the same supplied references. The quantum algorithm really retains them; the classical protocol really discards them.

## Growing reference budgets and matched baselines

The fixed-$m$ asymptotic cannot be substituted at $m=\Theta(\log M)$. A finite moment converse instead gives a logarithmic necessary reference order for constant revealed-query classical success: using the integer moment $s=2$,

$$
P_{\mathrm{classical}}^{\mathrm{revealed}}
\le\frac{D_m}{\sqrt{M D_{2m}}}
\le\sqrt{\frac{\binom{2m}{m}}{M}}
\le\frac{2^m}{\sqrt M}.
$$

The middle inequality follows from the product formula for $D_s$. Consequently constant success requires $m=\Omega(\log M)$. Established classical-shadow methods give the matching $O(\log M)$ reference-copy order for a later exact query in a library with a fixed separation margin, using the known rank-one query projector as an observable. This is a logarithmic reference-copy comparison, not an exponential total-sample advantage. See [related work](../references/RELATED_WORK.md) for attribution and the promise behind that comparator.

The finite-query common-component upper bound in [classical preprocessing](classical_preprocessing.md) also produces a separation at $m,t=\Theta(\log M)$ and $d\gg(\log M)^2$, with constants chosen so that $B$ is sufficiently larger than $M$. Its measure-and-prepare mechanism is inherited from prior work.

## What follows, and what remains outside the model

The contribution is a multiclass copy frontier paired with a sharp classical-record saturation law across a delayed-query boundary. Quantum-memory advantages, state-comparison methods and measurement-order effects are established prior insights; the [comparison](../references/RELATED_WORK.md) makes that shared foundation explicit.

This result assumes independent Haar pure states, equal reference budgets, a uniform label and one lookup. It does not prove a worst-case arbitrary-codebook converse, robustness for mixed/noisy states, reusable references, compressed quantum memory, or a runtime advantage over classical algorithms given full reference descriptions. The constructive scan performs up to $M$ tests and stores supplied quantum inputs; no index or amplitude amplification is free.
