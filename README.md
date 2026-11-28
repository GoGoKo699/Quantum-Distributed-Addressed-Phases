# Quantum Distributed Addressed Phases

**How many Bell pairs does each link need to implement a coherent lookup across a network of quantum processors?**

Each module holds a $`k`$-qubit address and a table of $`2^k`$ data qubits. The gate XORs the addresses coherently, then applies a sign determined by the parity of the selected data bits across the modules. All input registers stay on their modules and may be entangled with an external reference.

## Results

On any tree, **$`2k`$ Bell pairs per edge** are necessary and sufficient for exact synthesis. With a hard Bell-pair budget $`b_e`$ on each edge, the compiler attains the optimal half-diamond error

```math
\delta_\star=1-2^{\min\{2k,\min_e b_e\}-2k}.
```

The compiler gathers and broadcasts address bits coherently, applies local phases, and erases temporary copies by measurement and feedforward. Below the exact budget, it measures one address parity when needed and uses randomized table slices. A flat Schmidt spectrum of the target channel's Choi state supplies the matching lower bound on every tree cut.

| Classical communication | Bell-pair cost with a $`k`$-bit address |
| --- | --- |
| Interactive, exact | Exactly $`2k`$ per tree edge |
| One simultaneous exchange, exact | At least $`k+2^k-1`$ across a cut |
| One simultaneous exchange, small fixed error | At least order $`2^k`$ across a cut |

For example, with a four-bit address, the interactive compiler is exact at eight Bell pairs per edge. If any edge has only seven, the optimal error rises to one half. One simultaneous exchange needs at least nineteen Bell pairs across a cut for the exact gate.

The one-exchange lower bound grows linearly with the size of the explicit table, even at half-diamond error $`1/64`$. On two modules, an exact one-exchange protocol uses $`2(2^k-1)`$ Bell pairs. It matches the lower bound in its growth with table size.

The model supplies ideal Bell pairs and permits local quantum computation and classical messages. Each processor holds its table explicitly and implements the local lookup with ordinary gates. The link bounds measure Bell pairs independently of the local gate count.

## Run the addressed phase

Set aside the supplied Bell pairs on each edge and initialize local scratch in the zero state. Keep the original address and table registers at their modules.

1. **Gather and broadcast.** Root the tree and copy each local address into an accumulator with CNOTs. For each copied bit, CNOT it into the sending Bell half, measure that half in the computational basis, and send the result. The receiver applies X to its half on outcome one. Gather bottom-up, XORing each received child accumulator into its parent's accumulator. Then copy the root's global XOR address top-down. This uses one Bell pair per bit, per edge, in each direction.
2. **Apply the local phase and clear scratch.** At each module, compute the address prefixes with Toffolis using positive and negative address controls, apply CZ from each leaf flag to its table entry, and uncompute the flags. Measure routing scratch in the X basis. Use the known linear form of each scratch bit to compute which original address bits need Z corrections, and send the correction bits to their modules. Return the original address and table registers. The [tree compiler](science/interactive-tree.md#coherently-collecting-and-distributing-an-address) counts the local decoder and separates message timing from the Bell-pair budget.
3. **Respect a smaller edge budget.** Use the common budget capped at twice the address width. With `2i + m` pairs per edge, where `m` is zero or one, route `i` low bits in both directions. If `m` is one, gather the next bit, measure its global parity at the root, broadcast that result, and clear its remaining scratch as above. Draw the shared high slice and high character independently and uniformly for the table lookups and local Z phases, respectively. Keep all branches and discard the classical record after feedforward. The [budgeted circuit](science/interactive-tree.md#operating-with-fewer-bell-pairs) attains the stated unconditional error.

For **two modules with one simultaneous exchange**, relabel each local table by XOR with its own address. Apply the baseline phase from table entry zero locally. For every nonzero index, compute the address-equality flag on one side and the parity of that entry with entry zero on the other. For each [remote CZ](science/simultaneous-exchange.md#bipartite-protocol-in-one-exchange), the control side CNOTs its flag into its Bell half and measures that half in Z. The target side applies CZ from its Bell half to its flag and measures that half in X. Once both sides have produced all results, exchange them together. Each side applies Z to its flag when the received result is one, then uncomputes its flags and table relabeling. The protocol performs these terms in both directions and consumes one Bell pair per remote CZ.

## Read and reproduce

- [Gate model and resources](science/model.md)
- [Tree compiler and optimal error](science/interactive-tree.md)
- [One simultaneous exchange](science/simultaneous-exchange.md)
- [Learning milestones](learning/MILESTONES.md) and [Watrous bridge](learning/WATROUS_BRIDGE.md)

Run both exact-arithmetic checks with Python 3.

```bash
python3 verify/verify_interactive_tree.py
python3 verify/verify_simultaneous_exchange.py
```

The tree check covers measurement and cleanup branches on a three-module path and the Walsh, slice and Choi calculations through three address bits. The one-exchange check covers the remote controlled-Z measurement branches and the local lookup reduction. The linked science pages give the general proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
