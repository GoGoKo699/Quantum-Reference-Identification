# Exactly revealed query

Consider a stronger experiment: after the reference systems have been retained, the exact query state $`\psi`$ is supplied as a classical description. Conditional on $`\psi`$, the reference hypotheses are

```math
\rho_j^{(\psi)}
=\psi^{\otimes m}_{R_j}\otimes
\bigotimes_{i\neq j}\frac{I_{R_i}}{D_m}.
```
These hypotheses commute. Measure each reference block against the rank-one projector $`\psi^{\otimes m}`$. The true label always passes. Every other label independently passes with probability $`p=1/D_m`$. The common eigenbasis resolves all available information; conditional on its passing set the posterior is uniform on that set. Uniform tie breaking is therefore optimal, and

```math
\begin{aligned}
P_{\mathrm{quantum,revealed}}
&=\mathbb E\!\left[\frac1{1+\mathrm{Bin}(M-1,1/D_m)}\right]\\
&=\frac{D_m}{M}
\left[1-\left(1-\frac1{D_m}\right)^M\right].
\end{aligned}
```
For example, use $`1/(k+1)=\int_0^1x^k\,dx`$ in the binomial average to obtain the second line. This formula includes $`D_m=1`$ and $`M=1`$ without taking limits. When $`M/D_m\to0`$ with $`M\geq2`$, its error is asymptotic to $`(M-1)/(2D_m)`$.

The revealed-query experiment upper bounds every finite-query success probability. It supplies extra information; it is not the finite $`t`$ optimum or a free tomography primitive. At fixed $`d,m,M`$, consistent pure-state tomography as $`t\to\infty`$, followed by the conditional reference measurement, approaches the revealed-query optimum. Thus it is also the limiting endpoint of the finite-query problem, without a claimed finite-copy tomography rate.


Return to [finite-query identification](quantum_identification.md) or compare the [classical-record endpoint](classical_preprocessing.md).
