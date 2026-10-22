# SL₂ plethysm 的钩长分母：低阶例外与修正版证明

版本日期：2026-10-22。

本文证明一个精确的分母清除命题：对每个大小至少为 3 的分拆，固定外部 Schur 函子的 SL₂ plethysm 生成函数具有由该分拆钩长控制的分母。该命题对应 Gutiérrez–Orellana–Saliola–Schilling–Zabrocki 的 [*A geometric and generating function approach to plethysm*, arXiv:2511.02649v2](https://arxiv.org/abs/2511.02649v2) 中 Conjecture 4.1，需排除原文字面范围中的三个低阶例外。

本文是公开供核验的证明草稿，尚未经外部同行评审或形式化验证，首次性尚未确认。它不解决任意 plethysm 系数的正组合规则，也不证明原论文的几何 Conjecture 1.1。所用粗分母定理属于原论文已有结果；Schur 主特化、部分分式和有限差分均为经典工具。本文的具体工作是用这些工具控制形状相关的极点，并完成二元分母的精化。

## 1. 定义与结论

设 $\mu=(\mu_1,\mu_2,\ldots)\vdash w$ 是大小为 $w$ 的分拆，其 Young 图也记为 $\mu$。对格 $c=(i,j)\in\mu$，定义

$$
\operatorname{ct}(c)=j-i,\qquad
h_c=\mu_i-j+\mu'_j-i+1,\qquad
b(\mu)=\sum_i(i-1)\mu_i.
$$

其中 $\mu'$ 是共轭分拆。指标 $h\ge0$ 与钩长 $h_c$ 是不同的量。

令 $s_\mu$ 为 Schur 多项式，并置

$$
S_h(x)=s_\mu(x^{-h},x^{-h+2},\ldots,x^h).
$$

这是 Schur 函子作用于 $(h+1)$ 维不可约 SL₂ 表示后得到的特征标。因此存在唯一的非负整数 $a_{\mu[h]}^{[k]}$，使

$$
S_h(x)=\sum_{k\ge1}a_{\mu[h]}^{[k]}[k]_x,
\qquad
[k]_x=\frac{x^k-x^{-k}}{x-x^{-1}}.
$$

这里 $[k]_x$ 是 **$k$ 维**不可约 SL₂ 表示的特征标，其最高权为 $k-1$。每个固定 $h$ 的和都是有限和。由此立即得到

$$
a_{\mu[h]}^{[k]}=[x^k](x-x^{-1})S_h(x)
\qquad(k\ge1).
\tag{1}
$$

定义二元形式级数及多项式

$$
A_\mu(z,q)=\sum_{h\ge0}\sum_{k\ge1}
a_{\mu[h]}^{[k]}z^h q^k,
$$

$$
Q_w(z,q)=
\prod_{\substack{1\le r\le w\\r\equiv w\pmod2}}(1-q^r z),
$$

$$
D_\mu(z)=
\begin{cases}
\displaystyle\prod_{c\in\mu}(1-z^{h_c}),&w\text{ 为偶数},\\[4pt]
\displaystyle\prod_{c\in\mu}(1-z^{2h_c}),&w\text{ 为奇数}.
\end{cases}
$$

当 $w\ge3$ 时，令

$$
T_\mu(z)=\frac{D_\mu(z)}{(1-z)^2}\in\mathbb Z[z].
$$

最后的整系数性质成立，因为 $D_\mu$ 的每个因子都含有 $1-z$，且共有 $w\ge3$ 个因子。

**定理。** 对任意整数 $w\ge3$ 及任意分拆 $\mu\vdash w$，

$$
\boxed{\quad T_\mu(z)Q_w(z,q)A_\mu(z,q)\in\mathbb Z[z,q].\quad}
\tag{2}
$$

这给出的是一个可用分母，未断言它是约分后的最小分母。

## 2. 引用输入：已有的粗分母定理

原论文 §4.2 已证明

$$
R_w(z)Q_w(z,q)A_\mu(z,q)\in\mathbb Z[z,q],
\tag{3}
$$

其中

$$
R_w(z)=
\begin{cases}
\displaystyle(1-z)\prod_{i=1}^w(1-z^i),&w\text{ 为偶数},\\[4pt]
\displaystyle\prod_{i=1}^w(1-z^{2i}),&w\text{ 为奇数}.
\end{cases}
$$

该结果在 [v2 PDF 的印刷第 19 页](https://arxiv.org/pdf/2511.02649v2#page=19) 编号为 **Theorem 4.9**，在 [v2 HTML §4.2](https://arxiv.org/html/2511.02649v2#S4.SS2) 编号为 **Theorem 4.8**；这里按公式 (3) 识别所用结果。它是引用输入，而非本文原创结论。附录解释原文证明中正部截取公式的取整符号，并不以其错误的中间索引作推理。

式 (3) 蕴含：对某个 $P_\mu\in\mathbb Z[z,q]$，

$$
B_\mu(z,q):=Q_w(z,q)A_\mu(z,q)
=\frac{P_\mu(z,q)}{R_w(z)}\in\mathbb C(z)[q].
\tag{4}
$$

因此，**$B_\mu$ 只有有限多个非零的 $q$ 系数**。后文会明确使用这个有限支撑性质；它不能仅由逐个固定 $q^k$ 的分析取代。

## 3. 钩长主特化与固定标签的最终准多项式

置

$$
H_\mu(x)=\prod_{c\in\mu}(1-x^{2h_c}).
$$

经典 Schur 钩长—内容主特化给出

$$
S_h(x)=
\frac{x^{-wh+2b(\mu)}}{H_\mu(x)}
\prod_{c\in\mu}\left(1-x^{2(h+1+\operatorname{ct}(c))}\right).
\tag{5}
$$

这一公式取自 $s_\mu(1,t,\ldots,t^{N-1})$ 的主特化，令 $t=x^2$、$N=h+1$，再利用 $s_\mu$ 的 $w$ 次齐次性。经典背景可参见 Stanley 的 [*Theory and Application of Plane Partitions, Part 2*, §15](https://math.mit.edu/~rstan/pubs/pubfiles/12-2.pdf)。

若 $h+1<\ell(\mu)$，式 (5) 仍成立：Schur 特化为零，分子中格 $(h+2,1)$ 对应的因子也为 $1-x^0=0$。

对 Young 图的格子子集 $U\subseteq\mu$，令

$$
E_U=2b(\mu)+2\sum_{c\in U}(1+\operatorname{ct}(c))\in2\mathbb Z,
\qquad
G_\mu(x)=\frac{x-x^{-1}}{H_\mu(x)}.
$$

展开式 (5) 的分子，得到

$$
(x-x^{-1})S_h(x)
=\sum_{U\subseteq\mu}(-1)^{|U|}
x^{(2|U|-w)h+E_U}G_\mu(x).
\tag{6}
$$

在 $x=0$ 作 Laurent 展开 $G_\mu(x)=\sum_n g_nx^n$。由于 $H_\mu(0)=1$，最低可能指数是 $-1$，故 $g_n=0$ 对 $n<-1$ 成立。由 (1) 与 (6)，

$$
a_{\mu[h]}^{[k]}
=\sum_{U\subseteq\mu}(-1)^{|U|}
g_{k+(w-2|U|)h-E_U}.
\tag{7}
$$

固定 $k\ge1$。若 $|U|>w/2$，右侧对应下标随 $h$ 趋于负无穷，该项最终为零；若 $|U|=w/2$，对应项与 $h$ 无关。因此只有 $|U|<w/2$ 的项需要分析正斜率的无限尾部。

所有 $H_\mu$ 的根都是单位根。对这样的根 $\alpha$，定义

$$
d_\alpha=\operatorname{ord}(\alpha^2),\qquad
m_\alpha=\#\{c\in\mu:d_\alpha\mid h_c\}.
$$

因子 $1-x^{2h_c}$ 在其非零根处为简单零点，所以 $G_\mu$ 在 $\alpha$ 处的极点阶至多为

$$
\rho_\alpha=
\begin{cases}
w-1,&\alpha=1\text{ 或 }-1,\\
m_\alpha,&\alpha\ne1,-1.
\end{cases}
\tag{8}
$$

第一种情形使用了 $x-x^{-1}$ 在 $\pm1$ 的简单零点。

部分分式说明，对充分大的整数 $n$，

$$
g_n=\sum_\alpha\alpha^{-n}p_\alpha(n),
\qquad\deg p_\alpha\le\rho_\alpha-1.
\tag{9}
$$

这里不存在极点的根可不计入，$p_\alpha$ 为复系数多项式。具体地，

$$
[x^n](1-x/\alpha)^{-j}
=\alpha^{-n}\binom{n+j-1}{j-1},
$$

而 Laurent 多项式部分只影响有限多个 $n$。

将式 (9) 代入 (7)。对每个固定 $k$，当 $h$ 充分大时，所得序列是有限个

$$
\beta^h P(h),\qquad
\beta=\alpha^{-(w-2s)},\quad 0\le s<w/2,
\tag{10}
$$

的线性组合，另有可能出现的常数序列。其中 $\deg P\le\rho_\alpha-1$。因为 $\beta$ 为单位根，该序列最终为准多项式；阈值可以依赖 $k$。

特别地，

$$
F_k(z):=[q^k]A_\mu(z,q)
=\sum_{h\ge0}a_{\mu[h]}^{[k]}z^h
$$

是有理函数。一个 $\beta^hP(h)$ 项只可能在 $z=\beta^{-1}$ 产生极点，其阶至多为 $\deg P+1$。有限多个初项的改变只增加一个多项式，不改变有限极点。

## 4. 单位根极点的钩长控制

考虑式 (10) 的一项。若其在 $z=\zeta$ 有极点，则

$$
\zeta=\alpha^{w-2s}.
\tag{11}
$$

令 $e=\operatorname{ord}(\zeta)$，$d=d_\alpha$。

若 $w$ 为偶数，$w-2s$ 也是偶数，所以 $e\mid d$。于是 $d\mid h_c$ 蕴含 $e\mid h_c$，从而

$$
m_\alpha\le\#\{c:e\mid h_c\}
=\operatorname{ord}_{z=\zeta}D_\mu(z).
\tag{12}
$$

若 $w$ 为奇数，由 $\alpha^{2d}=1$ 得 $e\mid2d$。因此 $d\mid h_c$ 蕴含 $e\mid2h_c$，从而

$$
m_\alpha\le\#\{c:e\mid2h_c\}
=\operatorname{ord}_{z=\zeta}D_\mu(z).
\tag{13}
$$

对于 $\alpha=\pm1$，同样的计数为 $m_\alpha=w$，实际极点阶还因式 (8) 至少降低了 1。零斜率项只能在 $z=1$ 产生至多一阶极点。

因此每个 $F_k$ 的有限极点及其重数均由 $D_\mu$ 覆盖。多个贡献汇到同一个 $\zeta$ 时，和的极点阶至多为各项极点阶的最大值，不能把这些阶数相加。下一步把 $z=1$ 处的界从 $w$ 改进为 $w-2$。

## 5. 一个钩长整除引理

**引理 1。** 若 $|\mu|=w\ge3$ 且 $d\ge2$，则至少有两个格的钩长不被 $d$ 整除。换言之，

$$
\#\{c\in\mu:d\mid h_c\}\le w-2.
\tag{14}
$$

**证明。** 若 Young 图至少有两个可移去的角，则这两个格的钩长均为 1，结论成立。

若只有一个可移去的角，则所有非零行长相等，即 Young 图为矩形。单行或单列且大小至少为 3 时，存在钩长为 $1,2,3$ 的格；长宽都至少为 2 的矩形，也在右下部存在这些钩长。任意 $d\ge2$ 不可能同时整除 2 和 3。因此，除钩长为 1 的格外，还至少有一个钩长不被 $d$ 整除的格。证毕。

对 $\alpha\ne\pm1$，有 $d_\alpha\ge2$，所以引理 1 与 (8) 给出

$$
\rho_\alpha\le w-2.
$$

因此这些根的贡献在任何点的极点阶均至多为 $w-2$，尤其在 $z=1$ 如此。

## 6. 两个特殊根的最高次项抵消

只剩 $\alpha=1,-1$。由式 (8)–(9)，可写

$$
p_\alpha(n)=K_\alpha n^{w-2}+\text{次数至多为 }w-3\text{ 的项},
$$

其中当实际次数更低时取 $K_\alpha=0$。式 (7) 中 $|U|=s<w/2$ 的该根贡献为

$$
(-1)^s\alpha^{-k-(w-2s)h+E_U}
p_\alpha\bigl(k+(w-2s)h-E_U\bigr).
$$

每个 $E_U$ 都是偶数，故 $\alpha^{E_U}=1$，并且

$$
\alpha^{-(w-2s)h}=\alpha^{-wh}.
$$

所以所有这些项具有同一个指数因子 $\alpha^{-wh}$；该因子乘着的多项式，其 $h^{w-2}$ 总系数等于

$$
K_\alpha\alpha^{-k}
\sum_{0\le s<w/2}(-1)^s\binom ws(w-2s)^{w-2}.
\tag{15}
$$

这里使用了大小为 $s$ 的格子子集共有 $\binom ws$ 个。我们证明式 (15) 中的有限和为零。

次数为 $w-2$ 的多项式，其 $w$ 阶有限差分为零，因此

$$
\sum_{s=0}^{w}(-1)^s\binom ws(w-2s)^{w-2}=0.
\tag{16}
$$

将 $s$ 与 $w-s$ 配对，利用

$$
(-1)^{w-s}(-w+2s)^{w-2}
=(-1)^s(w-2s)^{w-2},
$$

配对的两项相等。若 $w$ 为偶数，中央项为 $0^{w-2}=0$；这里 $w\ge3$ 保证指数为正。于是式 (16) 恰为式 (15) 中有限和的两倍，所需抵消成立。

因此，对每个 $\alpha=\pm1$，汇总后的贡献具有次数至多为 $w-3$ 的多项式因子，其生成函数极点阶至多为 $w-2$。当 $w$ 为偶数时两个根均映到 $z=1$；当 $w$ 为奇数时分别映到 $z=1,-1$。

再加上第 5 节的界以及至多一阶的零斜率贡献，因 $1\le w-2$，得到

$$
\operatorname{poleord}_{z=1}F_k(z)\le w-2
\qquad(k\ge1).
\tag{17}
$$

结合第 4 节，$T_\mu(z)F_k(z)$ 没有任何有限极点：在 $z=1$，$T_\mu$ 的零点阶是 $w-2$；在其他点，$T_\mu$ 与 $D_\mu$ 的零点阶相同。它在 $z=0$ 原本正则。因此

$$
T_\mu(z)F_k(z)\in\mathbb C[z]
\qquad(k\ge1).
\tag{18}
$$

这里使用了没有有限极点的复有理函数是多项式这一事实。

## 7. 有限支撑提升与整系数性

**引理 2（有限 $q$ 支撑提升）。** 设 $A(z,q)=\sum_{k\ge0}F_k(z)q^k$，$F_k\in\mathbb C(z)$；设 $T\in\mathbb C[z]$、$Q\in\mathbb C[z,q]$。若

1. 对每个 $k$，$TF_k\in\mathbb C[z]$；
2. $QA\in\mathbb C(z)[q]$，即 $QA$ 只有有限多个非零的 $q$ 系数；

则 $TQA\in\mathbb C[z,q]$。

**证明。** 写 $Q=\sum_{r,u}c_{r,u}q^rz^u$，并约定 $F_k=0$ 对 $k<0$ 成立。每个固定 $j$ 满足

$$
T[q^j](QA)=\sum_{r,u}c_{r,u}z^uTF_{j-r}\in\mathbb C[z].
$$

由第二个条件，这样的非零系数只有有限多个，故结论成立。证毕。

此引理不要求所有 $TF_k$ 的 $z$ 次数有统一上界，但有限 $q$ 支撑不可省略。例如每个 $[q^k](1-qz)^{-1}=z^k$ 都是多项式，而 $(1-qz)^{-1}$ 不是二元多项式。

现在对 $A=A_\mu$、$Q=Q_w$、$T=T_\mu$ 应用引理 2。式 (18) 提供条件 1，引用的粗分母定理所给的式 (4) 提供条件 2，于是

$$
T_\mu(z)Q_w(z,q)A_\mu(z,q)\in\mathbb C[z,q].
$$

最后，$A_\mu\in\mathbb Z[[z,q]]$，而 $T_\mu$、$Q_w$ 均为整系数多项式，所以左侧的形式级数各系数都是整数。既然已经证明其支撑有限，它便属于 $\mathbb Z[z,q]$。定理得证。

## 8. 三个低阶例外

原论文的 Conjecture 4.1 允许任意正整数 $w$。按这一定义范围，$w=1,2$ 的三个分拆均为例外。相关生成函数也列于原论文 [§3.1 Table 1](https://arxiv.org/html/2511.02649v2)。

若 $\mu=(1)$，则 $S_h=[h+1]_x$，所以

$$
A_{(1)}(z,q)=\frac q{1-qz},\qquad
\frac{D_{(1)}Q_1A_{(1)}}{(1-z)^2}
=\frac{q(1+z)}{1-z}\notin\mathbb Z[z,q].
$$

对 $w=2$，SL₂ 对称平方与外平方的经典分解为

$$
\operatorname{Sym}^2 V_h=\bigoplus_{j=0}^{\lfloor h/2\rfloor}V_{2h-4j},
\qquad
\bigwedge^2 V_h=\bigoplus_{j=0}^{\lfloor(h-1)/2\rfloor}V_{2h-2-4j},
$$

其中 $V_m$ 的最高权是 $m$，维数是 $m+1$；空和为零。这给出

$$
A_{(2)}(z,q)=\frac q{(1-z^2)(1-q^2z)},\qquad
A_{(1,1)}(z,q)=\frac{qz}{(1-z^2)(1-q^2z)}.
$$

两个分拆的钩长都是 $2,1$，故

$$
\frac{D_{(2)}Q_2A_{(2)}}{(1-z)^2}=\frac q{1-z},
\qquad
\frac{D_{(1,1)}Q_2A_{(1,1)}}{(1-z)^2}=\frac{qz}{1-z}.
$$

它们都不是多项式。由此，本文处理的是 **$w\ge3$ 时的完整修正版**；低阶反例本身与这个全称证明是两项不同的内容。

## 9. 奇数大小时的直接推论

**推论。** 若 $w\ge3$ 为奇数，则

$$
\frac{D_\mu(z)Q_w(z,q)A_\mu(z,q)}{(1-z^2)^2}
\in\mathbb Z[z,q].
\tag{19}
$$

**证明。** 第 6 节对 $\alpha=-1$ 的抵消同时证明了 $z=-1$ 处的极点阶至多为 $w-2$；第 5 节控制了其他根映到 $-1$ 时的贡献。因 $D_\mu$ 在 $\pm1$ 均有 $w$ 阶零点，$D_\mu/(1-z^2)^2$ 清除每个 $F_k$ 的全部有限极点。第 7 节的提升与整系数论证原样适用。证毕。

这个强化也由权重奇偶性自动反映出来：$a_{\mu[h]}^{[k]}\ne0$ 蕴含 $k-1\equiv wh\pmod2$。当 $w$ 为奇数时，

$$
A_\mu(-z,q)=-A_\mu(z,-q),\qquad
Q_w(-z,q)=Q_w(z,-q),
$$

而 $D_\mu$ 是偶多项式。因此 $z=1$ 的二阶改善对称地传到 $z=-1$。该推论不单独作为一项独立新颖性主张。

## 附录：所引粗分母证明中的正部截取索引

为便于复核引用输入，下面给出相关截取的正确边界。令 $\mathsf{PT}_{\ge0}^q$ 在逐 $z$ 展开时保留所有 $q$ 指数非负的项。对整数 $b,c$，

$$
\frac{q^b}{1-q^cz}=\sum_{n\ge0}q^{b+cn}z^n.
$$

若 $c>0$，置 $n_0=\max(0,\lceil-b/c\rceil)$，则

$$
\mathsf{PT}_{\ge0}^q\frac{q^b}{1-q^cz}
=\frac{q^{b+cn_0}z^{n_0}}{1-q^cz}.
$$

若 $c<0$ 且 $b\ge0$，则

$$
\mathsf{PT}_{\ge0}^q\frac{q^b}{1-q^cz}
=\sum_{n=0}^{\lfloor b/(-c)\rfloor}q^{b+cn}z^n;
$$

若 $c<0$ 且 $b<0$，结果为零。若 $c=0$，结果在 $b\ge0$ 时为 $q^b/(1-z)$，在 $b<0$ 时为零。

原论文 v2 的 Theorem 4.9（HTML Theorem 4.8）证明中，正斜率删项的末端应为 $n_0-1$，负斜率的上界应使用 $-c$；原文相应的取整符号存在符号笔误。这由上面的逐项展开直接核对。例如 $b=-1,c=1$ 的截取结果应为 $z/(1-qz)$。

这些修正不引入新的分母类型：正斜率保留分母 $1-q^cz$；负斜率给出多项式；零斜率保留 $1-z$，已包含在偶数情形的粗分母中。因而修正不改变所引用的粗分母结论。对总字符 $(q-q^{-1})S_h(q)$，$q^0$ 系数为零，所以总式使用 $\mathsf{PT}_{\ge0}$ 与 $\mathsf{PT}_{>0}$ 没有区别；对单个部分分式则必须明确边界。

## 来源与优先权边界

- Gutiérrez, Orellana, Saliola, Schilling, Zabrocki, [*A geometric and generating function approach to plethysm*, arXiv:2511.02649v2](https://arxiv.org/abs/2511.02649v2)：定义、Table 1、Conjecture 4.1、粗分母定理。
- Stanley, [*Theory and Application of Plane Partitions, Part 2*, §15](https://math.mit.edu/~rstan/pubs/pubfiles/12-2.pdf)：Schur 主特化的经典来源。
- Patera–Sharp, [*Generating functions for SU(2) plethysms with fixed exchange symmetry* (1981)](https://doi.org/10.1063/1.524897)；Gaskell–Sharp, [*Fixed symmetry and fixed class generating functions* (1984)](https://doi.org/10.1063/1.526424)：与本文对象高度相关的早期文献。当前未完成两篇全文的逐式比较，因此不能排除等价结论早已存在，也不能据此断言已经存在。

本文主张的是上面可逐步检查的数学论证及其精确范围；不据“原文列为猜想”或“有限检索未发现证明”宣称全球优先权。完整证明也不等同于已经获得外部数学界确认。
