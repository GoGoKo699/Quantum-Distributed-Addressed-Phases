# Addressed phases on a tree

Consider a finite tree with at least two modules. Module $`v`$ holds a $`k`$-qubit address $`a_v`$ and a table $`z_v`$ of $`2^k`$ qubits, with $`k\geq 1`$. Write $`A=\bigoplus_v a_v`$ and $`Z=\bigoplus_v z_v`$ for computational-basis labels. The target unitary $`U`$ multiplies each basis vector by $`(-1)^{Z[A]}`$ and preserves its registers. Inputs may be entangled across modules or with a reference.

The modules have arbitrary local operations and classical communication. Edge $`e`$ supplies at most $`b_e`$ Bell pairs, with $`b_e`$ a nonnegative integer. There is no other shared quantum resource. Local scratch registers and classical randomness are free. The cost is a hard budget per execution, and every outcome counts. With $`b=\min(2k,\min_e b_e)`$, the optimum is

```math
\inf_{\mathcal E}\frac12\lVert\mathcal E-\operatorname{Ad}_U\rVert_\diamond
=1-2^{b-2k}.
```

## Coherently collecting and distributing an address

One Bell pair implements a computational-basis copy from one module to its neighbor. For a source bit label $`u`$, apply a local CNOT from the source to the local Bell half, measure that half in the computational basis to obtain $`m`$, and send $`m`$ to the neighbor. Applying $`X^m`$ to the other half gives the isometry $`|u\rangle\mapsto|u\rangle|u\rangle`$ in every normalized branch. Each $`m`$ occurs with probability one half independent of the input. This is a coherent copy of basis labels, including when the source is in superposition.

Root the tree. Initialize a scratch accumulator at each vertex to a local copy of its address. Process children before parents. For each edge, copy the child's accumulator into a fresh register at the parent using the Bell protocol and XOR it into the parent's accumulator. The root then holds $`A`$. Now process parents before children and copy the root's accumulated address down the tree. Each vertex obtains $`A`$ while retaining all of its data. Apply the local phase $`(-1)^{z_v[A]}`$ at each vertex. The product gives $`U`$.

Each retained scratch bit is a known linear form in the original address bits at the time of cleanup. Measure all scratch bits in the $`X`$ basis. The product of their measurement phases is a character of the original addresses. The parties compute its coefficients from the classical outcomes and apply the corresponding local $`Z`$ corrections to the original address bits. This erases every scratch register and preserves the phase uniformly over all inputs. The two passes use one Bell pair per bit per edge in each direction. The cleanup consumes none.

The local addressed phase can be implemented with a reversible traversal of the binary prefix tree of the address. Store the active prefix using at most $`O(k)`$ local scratch qubits. Compute each child prefix by a Toffoli with a positive or negative address control, apply a CZ between its flag and the corresponding table entry at a leaf, then uncompute each prefix. This uses $`O(2^k)`$ local gates per module and charges coherent data selection explicitly. Classical message timing is separate from the Bell-pair budget.

## Operating with fewer Bell pairs

Write $`b=2i+m`$, where $`m\in\{0,1\}`$, and split $`A=(H,M,L)`$ into $`h=k-i-m`$ high bits, $`m`$ middle bits and $`i`$ low bits. Use the two-pass protocol only on $`L`$. If there is a middle bit, aggregate it to the root with one Bell pair per edge. Measure the root accumulator in the computational basis, then broadcast the outcome. The same $`X`$-measurement cleanup applies to the remaining aggregation scratch. The root measurement projects onto the requested global parity, and the cleanup introduces no further dephasing. Discarding the outcome implements a dephasing channel $`\mathcal D_M`$ on the middle parity. Its random-unitary form is the uniform mixture of conjugations by the $`2^m`$ characters of $`M`$, including the identity.

Let $`d=2^h`$. Choose an independent, uniformly random high address $`j`$ and a uniformly random high character $`t`$. In every module, use $`(j,M,L)`$ to select the table entry. The value of $`M`$ is the shared measurement result, and $`L`$ remains coherent. Also multiply by $`(-1)^{t\cdot H}`$, a product of local $`Z`$ phases. Denote the corresponding diagonal unitary, with the appropriate middle slice in each of its parity blocks, by $`V_{j,t}`$. The implemented channel is

```math
\mathcal E=\frac{1}{d^2}\sum_{j,t}\operatorname{Ad}_{V_{j,t}}\circ\mathcal D_M.
```

Character orthogonality gives the operator identity

```math
U=\frac{1}{d}\sum_{j,t}(-1)^{t\cdot j}V_{j,t}.
```

In the Kraus representation of $`\mathcal E`$, keep the middle identity-character sector and mix its $`d^2`$ Kraus operators using a unit row with entries $`(-1)^{t\cdot j}/d`$. The resulting Kraus family contains $`U/(d\sqrt{2^m})`$. Consequently $`\mathcal E=p\operatorname{Ad}_U+(1-p)\mathcal N`$ for a channel $`\mathcal N`$ when $`p<1`$, with $`p=d^{-2}2^{-m}=2^{b-2k}`$. For $`p=1`$, the channel is exactly $`\operatorname{Ad}_U`$. The half-diamond error is at most $`1-p`$. No accepted-only branch or access to the discarded outcome is required.

## Matching lower bound on each edge

Cut the tree at any edge. On each side, the map from local labels to their XOR address and XOR table is a surjective linear map. Let $`f(A,Z)=(-1)^{Z[A]}`$. Its normalized Walsh coefficient at address character $`t`$ and table character $`s`$ is

```math
\widehat f(t,s)=2^{-k}\sum_A(-1)^{t\cdot A}\,\mathbf 1[s=e_A],
```

where $`e_A`$ has its only nonzero table coordinate at $`A`$. There are $`4^k`$ nonzero coefficients, all of magnitude $`2^{-k}`$. In the normalized Choi vector of $`U`$, the corresponding characters of the labels on each side give orthonormal local vectors by surjectivity. Thus the Choi vector has $`4^k`$ equal squared Schmidt coefficients. Each Choi reference qubit is assigned to the same module as its matching input qubit.

Across the chosen cut, the initial Bell pairs have Schmidt rank $`2^{b_e}`$. LOCC, including classical randomness and removal of local scratch, yields a Choi output of Schmidt number at most $`2^{b_e}`$. Its squared overlap with the target Choi vector is therefore at most $`\min(1,2^{b_e-2k})`$: a pure vector of rank at most $`r`$ can collect at most the $`r`$ largest squared Schmidt weights, and the bound extends by convexity. Testing the projection onto the target Choi vector yields the same lower bound on error as the complement of that overlap. The diamond distance includes this input and test. The tightest edge gives $`1-p`$, simultaneously attained by the construction above using the same budget $`b`$ on all edges.

## Scope and verification

The theorem uses ideal Bell pairs and permits interactive classical feedforward. It gives a worst-case resource budget for an entire channel, including arbitrary references. On a graph with cycles, the converse still applies with the sum of Bell budgets across a cut. The tree construction can run on any available spanning tree. A characterization for general graphs would require an additional protocol or a stronger converse.

The coherent-copy primitive has a standard coherent-communication formulation [Harrow, 2004](https://doi.org/10.1103/PhysRevLett.92.097902). The addressing function is a standard example in Fourier sparsity and dimension [Sanyal, 2019](https://doi.org/10.4086/toc.2019.v015a011). The operator-Schmidt method for exact gate implementation is also established [Stahlke and Griffiths, 2011](https://doi.org/10.1103/PhysRevA.84.032316). The tradeoff here combines the flat Choi spectrum with a compilation procedure that realizes the required Kraus weight at every integer budget.

Run `python3 verify/verify_interactive_tree.py` to check the coherent-copy branches, the cleanup on a three-module path, and the Walsh and Kraus calculations through $`k=3`$.
