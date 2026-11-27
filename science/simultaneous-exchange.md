# One simultaneous classical exchange

The interactive tree compiler uses $`2k`$ Bell pairs per edge for the addressed-phase unitary. With one simultaneous classical exchange across a cut, exact implementation needs at least $`k+2^k-1`$ Bell pairs across that cut. The lower bound allows arbitrary local instruments and corrections. At sufficiently small fixed diamond error, a single exchange still needs $`\Omega(2^k)`$ Bell pairs. An explicit bipartite protocol uses $`2(2^k-1)`$ Bell pairs in one exchange, giving matching order for two modules.

Here a simultaneous exchange means that both sides independently produce their classical messages using local instruments before either side receives the other's message. Each side may then apply a local channel using both messages. The two sides may share entanglement before the inputs arrive. A message carries classical data only. For a tree edge, grant joint operations to all modules on each side and model traffic across the edge by this exchange. The lower bounds concern that enlarged two-party model and apply separately to every edge obeying the exchange restriction.

## A state before the exchange

Consider a diagonal unitary with basis phases $`u_{xy}`$, where $`|u_{xy}|=1`$. Choose a set $`\mathcal Y`$ of $`s`$ Bob basis labels and strictly positive probabilities $`p_x`$ over a set of Alice basis labels. Let $`Q`$ and $`R`$ be local reference labels on the Alice and Bob sides. Take the initial state on the two sides' inputs and references to be

```math
|\chi\rangle
=\left(\sum_x\sqrt{p_x}|x\rangle_Q|x\rangle_A\right)
 \otimes \left(s^{-1/2}\sum_{y\in\mathcal Y}|y\rangle_R|y\rangle_B\right).
```

Denote the pure shared resource by $`|\eta\rangle_{L_0R_0}`$. Retain local instrument environments, so Bob's first instrument has one linear map $`K_b`$ into his retained space for each classical message $`b`$, with $`\sum_bK_b^\dagger K_b=I`$. Given $`b`$, Bob's pre-exchange operation produces an unnormalized pure vector $`|\beta_b\rangle_{R B_{\mathrm{mid}} L_0}`$ if Alice's first instrument is omitted. Write

```math
\sigma_b=\mathrm{Tr}_{L_0}|\beta_b\rangle\langle\beta_b|,
\qquad
\sigma=\sum_b |b\rangle\langle b|\otimes \sigma_b .
```

The same reduced state $`\sigma`$ results if Alice's first instrument is performed, its message and output discarded. This uses trace preservation on Alice's side and simultaneous messages. In particular, $`\sigma`$ is independent of the Alice input label $`x`$.

For each $`x`$, let $`D_x=\mathrm{diag}(u_{xy})_{y\in\mathcal Y}`$ act on $`R`$. Suppose the actual output on the task registers and references has expectation at least $`1-\delta`$ in the ideal pure output on $`|\chi\rangle`$. Then there is a joint state $`\tau`$ on the same registers as $`\sigma`$ for which

```math
\sum_x p_x\,T(\sigma,D_x\tau D_x^\dagger)\leq \sqrt{\delta},
\qquad (1)
```

with $`T(\rho,\zeta)=\|\rho-\zeta\|_1/2`$. Also, measuring $`R`$ in its label basis in $`\sigma`$ gives a joint distribution of $`(Y,b)`$ within total variation distance $`\sqrt{\delta}`$ of a uniform $`Y`$ independent of $`b`$.

To see both statements, purify the implementation on this fixed input. Keep transcript copies and take the final local corrections, conditioned on both message labels, to be isometries with local discarded environments. Project the purified output on the ideal vector in the task registers and references. Normalizing the projection gives the ideal vector tensored with a fixed junk vector, at trace distance at most $`\sqrt{\delta}`$ from the actual purification. The claims at large $`\delta`$ used below are trivial, so the projection can be taken nonzero. Dephase $`Q`$ and the two transcript labels in both states. In each transcript branch, apply a trace-preserving left inverse of Bob's final correcting isometry to Bob's output and its correction environment. Such an inverse applies the inverse isometry on its range and sends the orthogonal part to a fixed state. Keep $`b`$ and discard everything except $`Q,R,B_{\mathrm{mid}},b`$. For the actual state, this recovers the pre-exchange $`\sigma`$ for each classical label $`x`$. For the ideal state, conditioning on $`x`$ changes the common state after this processing by $`D_x`$ on $`R`$, since $`\sum_y u_{xy}|y,y\rangle/\sqrt{s}=(D_x\otimes I)\sum_y|y,y\rangle/\sqrt{s}`$. The ideal junk is independent of the ideal task output and references. In particular its transcript marginal $`b`$ is independent of the uniform reference measurement $`Y`$. Trace-distance contraction gives (1) and the classical distribution claim.

The use of a single fixed input entangled with references gives an error estimate independent of the size of the task registers. In particular, half diamond distance at most $`\delta`$ implies the overlap assumption by testing the projector onto the ideal output.

## Exact lower bound from distinct phase columns

Say two phase columns $`y,y'`$ are equivalent if $`u_{xy}/u_{xy'}`$ is independent of $`x`$. Let $`\mathcal Y`$ contain one representative of each equivalence class. Exact implementation makes $`\delta=0`$. Equation (1) then gives $`\sigma=D_x\tau D_x^\dagger`$ for every $`x`$. Hence $`\sigma`$ commutes with all $`D_xD_{x_0}^\dagger`$, for any fixed $`x_0`$. Any pair of distinct labels in $`\mathcal Y`$ is distinguished by at least one such diagonal operator, so $`\sigma_b`$ is block diagonal in $`R`$ for every $`b`$. Within each nonzero branch the $`R`$ blocks have equal normalized weight $`1/s`$, because $`Y`$ is both uniform and independent of $`b`$. The entropy of the normalized state on $`RB_{\mathrm{mid}}`$ is at least $`\log_2 s`$.

Purity of $`|\beta_b\rangle`$ equates this entropy with that of $`L_0`$ in the same branch. Bob's averaged instrument leaves his remote marginal on $`L_0`$ untouched. Concavity of entropy now gives

```math
E(|\eta\rangle)=S(L_0)\geq \sum_b\Pr(b)\,S(L_0\mid b)\geq\log_2 s.
\qquad (2)
```

In the addressed phase write $`n=2^k`$. Across each tree cut, locally restricting the inputs suffices to realize every pair of aggregate addresses $`a,b\in\mathbb F_2^k`$ and aggregate tables $`z,w\in\mathbb F_2^n`$ by varying one module per side. The phase is

```math
u_{(a,z),(b,w)}=(-1)^{z[a\oplus b]+w[a\oplus b]}.
```

For $`b\ne b'`$, columns $`(b,w)`$ and $`(b',w')`$ have a ratio depending on $`z`$, since the two selected coordinates differ. For $`b=b'`$ their ratio is constant exactly when $`w\oplus w'`$ is constant on all $`n`$ coordinates. Thus $`s=2^{k+n-1}`$, proving the edge lower bound $`k+n-1`$. The stated entanglement lower bound also holds for mixed resource states when measured by entanglement of formation, since exact ideal output on the test state forces exact ideal output on the same test for every pure component of a resource decomposition.

## Fixed-error lower bound for addressed phases

Restrict to one varying address $`x`$ on Alice's side and one varying $`n`$-qubit table $`w`$ on Bob's side, with $`w_0=0`$. Fix all remaining inputs to zero. The resulting phase is $`u_{xw}=(-1)^{w_x}`$, with $`D_0=I`$. Fix the same uniform superposition over the $`2^{n-1}`$ free table labels for Bob in every test. Let $`t=\sqrt{\delta}`$ if the protocol has half diamond error at most $`\delta`$. For each $`i\ne 0`$, use $`p_0=p_i=1/2`$ in (1), with other addresses omitted from that test. The state $`\sigma`$ is the same in every test because it uses only Bob's instrument and input. The comparison state $`\tau_i`$ can depend on $`i`$. The two test outcomes give

```math
T(\sigma,\tau_i)+T(\sigma,D_i\tau_i D_i)\le2t,
\qquad T(\sigma,D_i\sigma D_i)\le2t .
\qquad (3)
```

The second inequality follows by the triangle inequality and unitary invariance. The phase $`D_i`$ has signs $`+1,-1`$ on the two subspaces of $`R`$ with $`w_i=0,1`$, whose projectors are $`P^i_0,P^i_1`$. For fixed $`i`$, let $`\omega_{b,\ell}`$ be Alice's subnormalized state on $`L_0`$, formed by projecting $`|\beta_b\rangle`$ with $`P^i_\ell`$ and tracing $`RB_{\mathrm{mid}}`$. Uhlmann's theorem in its overlap form gives

```math
\big\|\sqrt{\omega_{b,0}}\sqrt{\omega_{b,1}}\big\|_1
=\big\|P^i_0\,\sigma_b\,P^i_1\big\|_1 .
```

The equality follows by maximizing the overlap of the two subnormalized purifications over a unitary on $`RB_{\mathrm{mid}}`$. The optimal binary discrimination error for these two weighted states is at most their root fidelity. Summing over $`b`$, the total error $`e_i`$ for guessing $`W_i`$ given $`b,L_0`$ is at most $`T(\sigma,D_i\sigma D_i)/2\le t`$. The factor $`1/2`$ accounts for the two off-diagonal blocks changing sign. The trace norm of the difference is four times the trace norm of one block.

Write $`W`$ for the free $`n-1`$ table bits measured in $`R`$. Apply the distribution claim following (1) using only address $`0`$. It gives that $`(W,b)`$ is within total variation distance $`t`$ of an independent uniform $`W`$ and some transcript distribution. Classical conditional entropy continuity gives, for $`t\le1/2`$,

```math
H(W\mid b)\ge (n-1)(1-t)-h_2(t).
```

One proof decomposes the two classical distributions into a common part of weight $`1-T`$ and residual parts of weight $`T`$, where $`T`$ is their actual total variation distance. Concavity of conditional entropy and the binary mixing entropy bound give a loss of at most $`T(n-1)+h_2(T)`$.

The chain rule and strong subadditivity bound $`H(W\mid b,L_0)`$ by the sum of the conditional entropies of its bits. For each bit, data processing and the binary decoding error bound this entropy by $`h_2(e_i)`$. Equation (3) thus gives $`H(W\mid b,L_0)\le(n-1)h_2(t)`$ when $`t\le1/2`$. Finally, the conditioned ensemble of $`L_0`$ encodes a classical variable, so

```math
I(W:L_0\mid b)\le S(L_0\mid b)\le S(L_0)=E(|\eta\rangle).
```

Together these bounds give the explicit robust estimate

```math
E(|\eta\rangle)\ge(n-1)\bigl[1-t-h_2(t)\bigr]-h_2(t),
\qquad t=\sqrt{\delta},\quad 0\le\delta\le 1/4 .
\qquad (4)
```

For example, $`\delta\le1/400`$ yields a lower bound of more than $`0.66(n-1)-0.29`$ ebits. The same bound allows shared classical randomness and holds with entanglement of formation for a mixed resource. For either extension, condition on the shared seed or a chosen pure resource component. For each test separately, its ideal-projector failure probability averages to at most $`\delta`$ over that conditioning label. The average square root, hence the average transcript distance in the address-$`0`$ test and the average decoding error in each bit test, is at most $`t`$. The classical entropy continuity loss and the bit entropy upper bound can be averaged using the concavity of $`h_2(\min(v,1/2))`$ as a function of $`v\in[0,1]`$. The Holevo bound then applies to the averaged entanglement. Minimizing over pure decompositions gives the entanglement of formation claim.

## Bipartite protocol in one exchange

For two modules, each locally changes the table indexing to $`z'[j]=z[j\oplus a]`$ and $`w'[j]=w[j\oplus b]`$, respectively. These are reversible, address-controlled permutations of the explicit table wires. The exponent of the desired sign is $`z'[b]\oplus w'[a]`$. For the first term use the identity

```math
z'[b]=z'[0]\oplus\bigoplus_{i\ne0} [b=i]\bigl(z'[i]\oplus z'[0]\bigr).
```

Implement the baseline phase $`(-1)^{z'[0]}`$ locally. Compute the address predicates and table parities into local ancillas. Each product in the sum is a remote controlled-$`Z`$ between an address predicate at one module and a table parity at the other. Apply the same decomposition in the other direction. Uncompute the flags, parities and relabeling after the phases.

A remote controlled-$`Z`$ takes one Bell pair and one simultaneous exchange. For computational labels $`q,r`$ of the control and target flags, the control side CNOTs its flag into its Bell half and measures that half in the $`Z`$ basis with result $`m`$. The target side applies $`CZ`$ from its Bell half to its flag and measures the half in the $`X`$ basis with result $`s`$. Conditioned on $`m,s`$, the phase applied to the flags is $`(-1)^{(q\oplus m)(r\oplus s)}`$. After exchanging the outcomes, local $`Z^s`$ on the control flag and $`Z^m`$ on the target flag leave the desired $`CZ`$ up to the branch's global phase. The target-side operations do not depend on $`m`$, so all $`2(n-1)`$ remote gates share the same simultaneous exchange. Retaining the computational inputs and uncomputing the flags and local permutations makes this a coherent protocol on arbitrary inputs and references. The upper bound here is for two modules.

Direct enumeration gives four projective columns for one address bit and 32 for two address bits. The same check agrees with the lookup expansion on all 64 and 4,096 basis input pairs, respectively. Checking all 16 combinations of remote flags and Bell outcomes gives the corrected branch amplitude, including its input-independent magnitude and global phase.

## Relation to earlier bounds

Gonzales and Chitambar's Theorem 3 and equations (73)–(79) establish an exact lower bound for binary-controlled gates with distinct target eigenphases. The key orthogonality in their proof is recovered here with two phase rows. Equation (2) uses all rows to distinguish projective columns, including cases such as the addressed sign gate where each individual phase has only two values. Equation (4) uses the same causal constraint in a fixed-error setting and converts the separate two-valued phase tests into random-access decoding of the table. [Gonzales and Chitambar, *Bounds on Instantaneous Nonlocal Quantum Computation*](https://arxiv.org/abs/1810.00994)

Cleve and May's Theorems 15 and 18 bound entanglement via controllable correlation and controllable entanglement in a model that allows simultaneous quantum messages. Their hypotheses and error terms differ from the single classical exchange and fixed-error phase tests used here. [Cleve and May, *Lower bounds on non-local computation from controllable correlation*](https://arxiv.org/abs/2602.00255)

