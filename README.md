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
