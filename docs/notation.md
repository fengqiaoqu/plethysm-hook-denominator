# 符号约定

本文使用原论文的维数标签约定：$[k]_x$ 对应维数为 $k$、最高权为 $k-1$ 的不可约 SL₂ 表示。

| 符号 | 含义 |
|---|---|
| $\mu\vdash w$ | 大小为 $w$ 的分拆及其 Young 图 |
| $\mu'$ | 共轭分拆 |
| $c=(i,j)\in\mu$ | 第 $i$ 行、第 $j$ 列的格 |
| $\operatorname{ct}(c)=j-i$ | 格的内容 |
| $h_c=\mu_i-j+\mu'_j-i+1$ | 格的钩长 |
| $b(\mu)=\sum_i(i-1)\mu_i$ | 主特化中的分拆统计量 |
| $h\ge0$ | 输入 SL₂ 不可约表示的最高权，其维数为 $h+1$；不是钩长 $h_c$ |
| $k\ge1$ | 输出 SL₂ 不可约表示的维数，其最高权为 $k-1$ |
| $S_h(x)$ | $s_\mu(x^{-h},x^{-h+2},\ldots,x^h)$ |
| $a_{\mu[h]}^{[k]}$ | $[k]_x$ 在 $S_h(x)$ 中的不可约表示多重数 |
| $A_\mu(z,q)$ | $\sum_{h\ge0,k\ge1}a_{\mu[h]}^{[k]}z^hq^k$ |
| $z$ | 记录输入最高权 $h$ 的形式变量 |
| $q$ | 记录输出维数 $k$ 的形式变量 |
| $x$ | SL₂ 特征标与一元系数提取使用的辅助变量 |
| $Q_w(z,q)$ | $\prod_{1\le r\le w,\ r\equiv w\pmod2}(1-q^rz)$ |
| $D_\mu(z)$ | 偶数 $w$ 时为 $\prod_c(1-z^{h_c})$；奇数 $w$ 时为 $\prod_c(1-z^{2h_c})$ |
| $T_\mu(z)$ | $D_\mu(z)/(1-z)^2$；主定理使用 $w\ge3$ |
| $R_w(z)$ | 已有粗分母：偶数 $w$ 时为 $(1-z)\prod_{i=1}^w(1-z^i)$；奇数 $w$ 时为 $\prod_{i=1}^w(1-z^{2i})$ |
| $F_k(z)$ | $[q^k]A_\mu(z,q)$；需要时约定 $k\le0$ 时为零 |
| $H_\mu(x)$ | $\prod_c(1-x^{2h_c})$ |
| $G_\mu(x)$ | $(x-x^{-1})/H_\mu(x)$ |
| $g_n$ | $G_\mu(x)$ 在 $x=0$ 的 Laurent 系数 $[x^n]G_\mu(x)$ |
| $U\subseteq\mu$ | Young 图格子的任意子集，不要求本身是 Young 图 |
| $E_U$ | 偶整数 $2b(\mu)+2\sum_{c\in U}(1+\operatorname{ct}(c))$ |
| $\operatorname{ord}(\alpha)$ | 单位根 $\alpha$ 的乘法阶 |
| $\operatorname{ord}_{z=\zeta}D(z)$ | 多项式 $D$ 在 $\zeta$ 的零点重数 |
| $\operatorname{poleord}_{z=\zeta}F(z)$ | 有理函数 $F$ 在 $\zeta$ 的极点阶；正则时记为 0 |
| $\mathsf{PT}_{\ge0}^q$ | 逐 $z$ 展开后保留 $q$ 指数非负的项 |

“最终准多项式”指存在周期 $L\ge1$ 及充分大阈值，使序列在每个模 $L$ 的剩余类上与一个多项式一致。主定理给出可用分母及相应上界，不断言最小分母、最小递推阶或最小周期。

完整论证见 [中文证明](proof.zh-CN.md)。
