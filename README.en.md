# Hook-length denominator bounds for SL₂ plethysm

**Complete proof draft; priority not established.** Version 0.1.0, 2026-10-22. [中文首页](README.md)

This repository presents a proof draft of a corrected form of Conjecture 4.1 in Gutiérrez–Orellana–Saliola–Schilling–Zabrocki, *A geometric and generating function approach to plethysm*, [arXiv:2511.02649v2](https://arxiv.org/abs/2511.02649v2). The claim covers every partition $\mu\vdash w$ with $w\ge3$; all three partitions of sizes 1 and 2 are exceptions to the original statement.

Write $a_{\mu[h]}^{[k]}$ for the multiplicity of the $k$-dimensional irreducible representation in $\mathbb S_\mu(\operatorname{Sym}^h\mathbb C^2)$ as an $\mathrm{SL}_2$ representation, and set

$$
A_\mu(z,q)=\sum_{h\ge0,\ k\ge1}a_{\mu[h]}^{[k]}z^h q^k,
\quad Q_w(z,q)=\prod_{\substack{1\le j\le w\\j\equiv w\pmod2}}(1-q^jz).
$$

For the hook lengths $h_c$ of $\mu$, let $D_\mu(z)=\prod_c(1-z^{\delta h_c})$, where $\delta=1$ for even $w$ and $\delta=2$ for odd $w$. The proposed theorem is

$$
\frac{D_\mu(z)Q_w(z,q)A_\mu(z,q)}{(1-z)^2}\in\mathbb Z[z,q]\qquad(w\ge3).
$$

The argument uses the original paper's proven coarse-denominator theorem, Schur principal specialization, partial fractions at roots of unity, and a finite-difference cancellation. It gives shape-dependent denominator, recurrence-order and eventual quasiperiod bounds. These bounds are not claimed to be minimal or to yield a measured speedup.

Read the [complete proof in Chinese](docs/proof.zh-CN.md), [notation](docs/notation.md), [background](docs/background.zh-CN.md), and [priority and scope statement](docs/priority-and-scope.zh-CN.md). References and reading limitations are recorded in [references.md](references.md).

## Reproduction

Python 3.10 or later; standard library only; no network access required:

```sh
python reproduce.py
```

See [results/README.md](results/README.md) for the methods and finite ranges. Passing these checks does not replace the general proof.

## Verification and novelty limits

Internal review has found no substantive error. No external peer review, author confirmation, or proof-assistant formalization has been obtained. The bounded literature search did not identify an equivalent earlier proof, but highly relevant papers from [1981](https://doi.org/10.1063/1.524897) and [1984](https://doi.org/10.1063/1.526424) have not been checked in full. Therefore, worldwide priority is not established.

This draft does not solve the general positive combinatorial rule for plethysm or the geometric Conjecture 1.1 of the source paper. AI assistance is disclosed in [NOTICE.md](NOTICE.md); citation guidance is in [CITATION.md](CITATION.md).
