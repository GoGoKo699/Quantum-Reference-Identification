# A three-qubit identification example

Two labeled reference devices each supply one unknown qubit. Independently, their states $\psi_1,\psi_2$ are Haar distributed. A later device supplies one more qubit promised to be an exact copy of one reference, selected with equal probability. Return label 1 or 2. This is $d=2$, $M=2$, $m=t=1$: three supplied physical qubits, no state descriptions and one lookup.

The [anchor bridge](ANCHOR_AND_BRIDGE.md) connects the calculation to Watrous §§2.1.2, 2.3.1, 3.1.1, 7.1.1 and 7.2.1. The general statements and their scope are in the [quantum proof](../science/quantum_identification.md).

## Averaging one hypothesis

Order the registers as $(R_1,R_2,T)$. If label 1 is true, $R_1,T$ contain the same state. Their two-copy average is uniform on the symmetric two-qubit subspace, whose basis is

$$
|00\rangle,\quad
\frac{|01\rangle+|10\rangle}{\sqrt2},\quad
|11\rangle.
$$

Its dimension is $D_2=3$, while $D_1=2$. The other reference averages to $I/2$. Let $F_{ab}$ swap registers $a,b$, and put

$$
P_1=\frac{I+F_{13}}2,\qquad
P_2=\frac{I+F_{23}}2.
$$

Each acts on the full eight-dimensional three-qubit space and has rank six. The two averaged hypotheses are

$$
\rho_1=\frac{P_1}{6},\qquad
\rho_2=\frac{P_2}{6},\qquad
C=\frac{2\cdot2}{3}=\frac43.
$$

The processor knows these averaged operators because it knows the distribution and register layout. It still does not know either sampled reference direction.

## An implementable decision

Measure whether $R_1,T$ are symmetric. If they are, return label 1; otherwise return label 2. For two qubits this is the projective pair $(I+F_{13})/2,(I-F_{13})/2$. A Hadamard flag, a controlled swap of those registers, and a final Hadamard/flag measurement realize the pair; $R_2$ is retained but this particular decision does not use it.

If label 1 is true, two equal pure states always lie in the symmetric subspace, so the answer is correct with probability one. If label 2 is true, $R_1$ and $T$ are independent Haar qubits. Their symmetric acceptance averages to its rank divided by the two-qubit dimension, $3/4$. This causes a false label-1 answer; rejection, of probability $1/4$, gives the correct label 2. The mean success is therefore

$$
P_{\mathrm{one\ test}}=
\frac12\cdot1+\frac12\cdot\frac14=\frac58.
$$

The procedure uses the three supplied qubits and one flag, with no description oracle. It establishes an achievable probability, not optimality. A larger scan must preserve the correct rejection instrument and account for disturbance; the [implementation account](../science/resources.md) handles that general case.

## What the general bounds say

The dimension-sensitive success bounds give

$$
\frac47\leq P_{\mathrm{opt}}\leq\frac23.
$$

Our explicit $5/8$ lies inside that interval. The PGM existence bound $4/7$ is a guaranteed lower bound, so a particular decoder may exceed it. Equivalently, combining the error statements gives $1/3\leq e_{\mathrm{opt}}\leq3/7$. The additional three-moment lower bound is $3/32$ here and is weaker than the rank-capacity lower bound $1/3$; universal constants need not be sharp in a small example.

For this binary instance the exact optimum can also be computed with the established Holevo–Helstrom theorem (Watrous, Theorem 3.4). The difference is

$$
\rho_1-\rho_2=\frac{F_{13}-F_{23}}{12}.
$$

On the one-excitation basis $|100\rangle,|010\rangle,|001\rangle$, the swap difference is

$$
\begin{pmatrix}
-1&0&1\\
0&1&-1\\
1&-1&0
\end{pmatrix},
$$

with eigenvalues $0,\sqrt3,-\sqrt3$. Flipping every qubit gives the same spectrum on the two-excitation sector; $|000\rangle$ and $|111\rangle$ give two additional zeros. Thus $\|\rho_1-\rho_2\|_1=\sqrt3/3$, where the trace norm adds absolute eigenvalues. Equal-prior binary discrimination yields

$$
P_{\mathrm{opt}}=
\frac12+\frac14\|\rho_1-\rho_2\|_1
=\frac12+\frac{\sqrt3}{12}
\approx0.644338.
$$

This is a worked application of an inherited binary theorem; no new binary optimum is claimed.

## Why the Gram zeros matter

Here $r=6$, so the concatenated Gram matrix used in the error converse has dimension $Mr=12$, even though the physical space has dimension eight. Its eigenvalues are $2$ four times, $3/2$ twice, $1/2$ twice, and $0$ four times. Their averages give

$$
\mathbb E\lambda=1,\qquad
\mathbb E\lambda^2=\frac74,\qquad
\mathbb E\lambda^3=\frac{13}4.
$$

These match $\beta=3/4$ and $\gamma=0$. Removing the four zeros would change the normalization and invalidate the identity relating the square-root deficit to error. The general proof uses all eigenvalues, rather than only the nonzero spectrum of $P_1+P_2$.

## Revealing the later query changes the experiment

Now supply the exact classical description of the query after the references have been retained. Test each reference against that known pure state. The true reference always passes, while the other passes with probability $1/D_1=1/2$. A unique pass identifies the label; if both pass, choose uniformly. Hence

$$
P_{\mathrm{quantum,revealed}}
=\frac12\cdot1+\frac12\cdot\frac12=\frac34.
$$

For comparison, independently measuring both references covariantly before that description arrives gives the particular classical-record strategy in the [classical account](../science/classical_preprocessing.md). In this case its achievable revealed-query success is $\mathbb E\max(X_1,X_2)=2/3$, with $X_1,X_2$ independent uniform variables on $[0,1]$. That value is not asserted to be the finite-parameter optimum among all collective training measurements.

The $2/3$ classical revealed-query value exceeds the finite-query quantum optimum $0.644338$ because it was granted extra query information. It cannot be used to judge the memory comparison at matched inputs. This toy calculation illustrates the operations and information boundary; the universal memory separation comes from the growing-$M$, fixed-$m$ theorem, with its stated dimension limit.

Return to the [anchor bridge](ANCHOR_AND_BRIDGE.md), [scientific reading route](../science/README.md), or [verification guide](../verification/README.md).
