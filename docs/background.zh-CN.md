# 背景、结果与数学意义

本文整理一个关于 **SL₂ plethysm 二元生成函数的钩长分母界** 的完整证明草稿。目标是 Gutiérrez–Orellana–Saliola–Schilling–Zabrocki 的 *A geometric and generating function approach to plethysm*，arXiv:2511.02649v2，Conjecture 4.1 的低阶修正版。[固定版本与原始命题](https://arxiv.org/html/2511.02649v2#S4)

草稿已作内部数学复核和独立有限计算，尚未经过外部同行评审或形式化验证；首次性也未确认。此公开版本的用途是让读者检查精确命题、证明和复现结果。查新边界见[范围与优先权说明](priority-and-scope.zh-CN.md)。

## 1. 从一般 plethysm 到本文对象

一般 plethysm 系数由 Schur 函数展开定义：

$$
s_\mu[s_\nu]=\sum_\lambda a^\lambda_{\mu,\nu}s_\lambda.
$$

为任意三组分拆建立合适的正组合规则，是原始问题 03-0002 所关注的一般性问题。本文处理其中一个受限的表示论族：固定外分拆 $\mu\vdash w$，内分拆取一行 $(h)$，再把表示限制到 $\mathrm{SL}_2$。记

$$
s_\mu(x^{-h},x^{-h+2},\ldots,x^h)
=\sum_{k\ge1}a_{\mu[h]}^{[k]}[k]_x,
\qquad [k]_x=\frac{x^k-x^{-k}}{x-x^{-1}}.
$$

其中 $h\ge0$，$k$ 是输出不可约 SL₂ 表示的维数，其最高权为 $k-1$。若满足非负整数和奇偶条件，相应的 GL₂ 输出分拆是

$$
\lambda=\left(\frac{wh+k-1}{2},\frac{wh-k+1}{2}\right).
$$

这说明本文涉及一行内分拆、至多两行输出所对应的系数；一般的 $\nu$ 和任意多行 $\lambda$ 不在本文分母定理的范围内。权重提取与上述对应关系是标准表示论输入，见[原论文 §2](https://arxiv.org/html/2511.02649v2#S2)和[Pak–Panova–Swanson 的 Lemma 1.3](https://arxiv.org/html/2511.02312v3#S1)。

把输入和输出标签一起求和，得到

$$
A_\mu(z,q)=\sum_{h\ge0}\sum_{k\ge1}a_{\mu[h]}^{[k]}z^hq^k.
$$

固定交换对称性、遍历 SU(2) 输入与输出的生成函数，至少已有 [Patera–Sharp 1981](https://doi.org/10.1063/1.524897) 和 [Gaskell–Sharp 1984](https://doi.org/10.1063/1.526424) 的研究。本文不以提出这一研究对象作为贡献；这两篇旧文全文尚未完成核对。

## 2. 要证明的精确分母界

对 Young 图的每个格 $c$，令 $h_c$ 为钩长，并记

$$
\delta=\begin{cases}1,&w\text{ 偶},\\2,&w\text{ 奇},\end{cases}
\qquad D_\mu(z)=\prod_{c\in\mu}(1-z^{\delta h_c}),
$$

$$
Q_w(z,q)=\prod_{\substack{1\le c\le w\\c\equiv w\pmod2}}(1-q^cz),
\qquad T_\mu(z)=\frac{D_\mu(z)}{(1-z)^2}.
$$

**草稿定理。** 对每个整数 $w\ge3$ 和每个 $\mu\vdash w$，

$$
T_\mu(z)Q_w(z,q)A_\mu(z,q)\in\mathbb Z[z,q].
$$

原 Conjecture 4.1 的字面表述允许所有正整数 $w$。按原定义直接计算，$\mu=(1),(2),(1,1)$ 的左侧依次为

$$
\frac{q(1+z)}{1-z},\qquad\frac q{1-z},\qquad\frac{qz}{1-z},
$$

均非多项式。因此 $w=1,2$ 必须排除。本文主体是对全部其余大小和全部形状的论证，低阶勘误只是附带结论。[原论文 Conjecture 4.1 与 Table 1](https://arxiv.org/html/2511.02649v2)

## 3. 已知结果与此次增量

原论文已经证明有理性、统一分母界和递推关系。本文使用的已知结论是

$$
R_w(z)Q_w(z,q)A_\mu(z,q)\in\mathbb Z[z,q],
$$

$$
R_w(z)=\begin{cases}
(1-z)\prod_{i=1}^w(1-z^i),&w\text{ 偶},\\
\prod_{i=1}^w(1-z^{2i}),&w\text{ 奇}.
\end{cases}
$$

它位于原论文 §4.2；固定 v2 PDF 编号为 Theorem 4.9，HTML 编号为 Theorem 4.8。[PDF 第19页](https://arxiv.org/pdf/2511.02649v2#page=19)、[HTML §4.2](https://arxiv.org/html/2511.02649v2#S4.SS2)

此次相对该定理的增量，是把只依赖大小 $w$ 的纯 $z$ 分母 $R_w$，精化为依赖具体形状钩长的 $T_\mu$。标准 q-hook 公式保证 $R_w/T_\mu\in\mathbb Z[z]$；需要证明的是实际生成函数具有相应约消。

证明采用经典 Schur 钩长—内容主特化、单位根部分分式、有限差分和原论文的统一分母定理。新的论证环节是：固定输出标签保留钩长信息，逐点追踪单位根极点，再利用最高次项抵消和有限 $q$ 支撑得到二元多项式结论。经典主特化公式可参见 [Stanley 1971，Part 2，§15](https://math.mit.edu/~rstan/pubs/pubfiles/12-2.pdf)。

## 4. 可量化的用途

令 $r=\lceil w/2\rceil$、$M=\sum_c h_c$。把 $A_\mu$ 写成 $z$ 的级数、系数属于 $\mathbb Z[q]$，新分母给出的最终递推阶数上界为

$$
N=\delta M-2+r.
$$

固定 $k$ 后，序列 $h\mapsto a_{\mu[h]}^{[k]}$ 最终为准多项式；其准周期可取为

$$
L=\delta\operatorname{lcm}\{h_c:c\in\mu\}
$$

的约数。粗分母给出的相应准周期上界是 $\delta\operatorname{lcm}(1,\ldots,w)$。下面四组整数由钩长定义直接计算：

| 外分拆 $\mu$ | 递推阶数上界：粗分母 → 钩长分母 | 固定输出标签的准周期上界：粗分母 → 钩长分母 |
|---|---:|---:|
| $(6)$ | 25 → 22 | 60 → 60 |
| $(3,2,1)$ | 25 → 15 | 60 → 15 |
| $(4,2,1)$ | 60 → 38 | 840 → 24 |
| $(4,4,4,4)$ | 145 → 70 | 720720 → 420 |

表中均为**允许的上界**，不是最小递推阶数或最小准周期，也不是运行速度测试。递推只在超过分子的相应次数后成立，表中未声称确定了最早起始位置。对正方形 $\mu=(n^n)$、$w=n^2$，$\sum_c h_c=n^3$，因而这一递推阶数上界从 $\Theta(w^2)$ 降到 $\Theta(w^{3/2})$；这仍不是计算全部 plethysm 系数的算法复杂度定理。

奇数 $w$ 时，权重奇偶对称性还允许以 $D_\mu/(1-z^2)^2$ 替换 $T_\mu$，使上述递推阶数上界再少 2。这是已述结论和对称性的直接推论，表格统一采用原猜想的 $(1-z)^2$ 形式。

## 5. 与正组合规则的区别

Pak–Panova–Swanson 已为至多两行输出的 plethysm 系数给出 marked-tree 正计数规则；其 Theorem 1.2 处理任意外分拆、一行内分拆的非平凡核心情形。[现行 v3 原文](https://arxiv.org/html/2511.02312v3#S1) 这一范围包含本文的 SL₂ 系数。因此不能把本工作称为首次给这些系数正组合意义。

分母界与正计数规则是不同结构结论。本文分子允许负系数，也未构造原论文 Conjecture 1.1 要求的几何锥分解。它没有解决一般 plethysm 正组合问题，没有给出全部最小分母，也没有建立新的普遍复杂度结论。

如果证明经外部审查成立且不存在已有等价结果，合理定位是：**专业子方向内有明确用途的统一结构定理**。当前公开材料不足以支持“解决了原始一般难题”“世界首次”或“重大一般突破”的表述。
