# SL₂ plethysm 钩长分母：修正版证明草稿

本仓库整理 Gutiérrez–Orellana–Saliola–Schilling–Zabrocki 的 *A geometric and generating function approach to plethysm*（[arXiv:2511.02649v2](https://arxiv.org/abs/2511.02649v2)）Conjecture 4.1 的一份证明草稿：处理所有大小 $w\ge3$ 的分拆，并列出原表述在 $w=1,2$ 的例外。[English summary](README.en.md)

**当前状态：内部数学复核未发现实质错误，有限计算核验通过；尚无外部同行评审或形式化证明，全球首次性未确认。** 1981、1984 年的两篇高度相关旧文尚未取得完整正文，不能据有限检索确认新颖性。一般 plethysm 正组合规则仍未解决。详见[范围与查新说明](docs/priority-and-scope.zh-CN.md)。

整理日期：2026-10-22。版本：0.1.0。维护账号：fengqiaoqu。

## 结果是什么

取分拆 $\mu\vdash w$，设 $a_{\mu[h]}^{[k]}$ 为 $\operatorname{Sym}^{k-1}(\mathbb C^2)$ 在 $\mathbb S_\mu(\operatorname{Sym}^h(\mathbb C^2))$ 限制为 $\mathrm{SL}_2$ 表示后出现的重数。这里 $h\ge0$、$k\ge1$，标签 $[k]$ 表示 **k 维**不可约表示。

定义

$$
A_\mu(z,q)=\sum_{h\ge0}\sum_{k\ge1}a_{\mu[h]}^{[k]}z^h q^k,\qquad
Q_w(z,q)=\prod_{\substack{1\le j\le w\\j\equiv w\pmod2}}(1-q^jz).
$$

令 $h_c$ 是 Young 图中格子 $c$ 的钩长；$w$ 为偶数时取 $\delta=1$，为奇数时取 $\delta=2$，并令

$$
D_\mu(z)=\prod_{c\in\mu}(1-z^{\delta h_c}).
$$

正文证明的精确命题为：对每一个 $\mu\vdash w$、$w\ge3$，

$$
\boxed{\frac{D_\mu(z)Q_w(z,q)A_\mu(z,q)}{(1-z)^2}\in\mathbb Z[z,q].}
$$

这是一个可用分母的上界，不是约分后的最小分母公式。$w=1,2$ 的三个例外、完整定义及所有推导见[完整证明](docs/proof.zh-CN.md)。

## 为什么有数学意义

原论文已经证明生成函数有理，并给出只依赖大小 $w$ 的粗分母。本草稿将它收紧为由具体分拆钩长决定的分母，从而得到更强的递推阶数、单位根极点和最终准周期上界。例如：

| 分拆 | 递推阶数上界：原定理→本草稿 | 固定输出标签的准周期上界：原定理→本草稿 |
|---|---:|---:|
| $(3,2,1)$ | 25→15 | 60→15 |
| $(4,2,1)$ | 60→38 | 840→24 |
| $(4,4,4,4)$ | 145→70 | 720720→420 |

这些都是保证可用的上界，不保证最小，也不是程序提速测试。若证明正确且没有已有等价结果，其增量是专业子方向的结构性加强。[背景、推论与限制](docs/background.zh-CN.md)给出详细说明。

## 证明的主线

1. 引用原论文已证的统一分母定理，保证乘 $Q_w$ 后只有有限多个 $q$ 系数。
2. 用 Schur 钩长—内容主特化，把固定输出标签的系数写成子集和。
3. 通过单位根处部分分式，把这些序列写成最终准多项式，控制其生成函数的极点。
4. 用钩长整除关系控制非平凡单位根；用有限差分消去 $z=1$ 处的最高阶项。
5. 利用有限 $q$ 支撑，从逐系数的极点控制提升为整系数二元多项式结论。

第1步是引用输入，主特化和有限差分是标准工具；本草稿的推导详见[证明正文](docs/proof.zh-CN.md)，不会将它们分别归为新发现。

## 阅读与复现

| 材料 | 内容 |
|---|---|
| [完整证明](docs/proof.zh-CN.md) | 定理、引理、所有参数范围与低阶例外 |
| [记号说明](docs/notation.md) | 表示标签、变量与分母记号 |
| [背景与价值](docs/background.zh-CN.md) | 已有结果、具体改进及推论 |
| [范围与查新](docs/priority-and-scope.zh-CN.md) | 已核查内容、未排除的旧文、首次性边界 |
| [复现说明](results/README.md) | 验证方法、数据范围与结果 |
| [参考文献](references.md) | 原始文献链接与实际阅读层次 |
| [AI 使用说明](NOTICE.md) | 生成、复核及责任边界 |

在仓库根目录运行：

```powershell
python reproduce.py
```

程序需要 Python 3.10 或更高版本，只使用标准库。默认重新生成 `results/` 下的记录；如需保留已发布记录，可运行 `python reproduce.py --output-dir ../local-verification`。具体输出说明见[复现说明](results/README.md)。检查包括钩长条件、有限差分、独立半标准 Young 表枚举、分母专化及上界比较。**有限核验用于发现错误，不能替代正文对所有分拆的证明。**

## 引用与反馈

引用建议见 [CITATION.md](CITATION.md)。讨论时请附具体分拆、公式或证明步骤，并区分数学反例、记号问题和优先文献线索。原作者没有为本仓库背书；本仓库不是期刊接收记录。
