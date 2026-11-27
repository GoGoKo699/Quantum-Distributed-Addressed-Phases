# Gate model and resources

Let $`T=(V,E)`$ be a finite tree with at least two vertices. Module $`v`$ holds an address register $`a_v\in\{0,1\}^k`$ and a data register $`z_v\in\{0,1\}^D`$, where $`D=2^k`$ and $`k\ge 1`$. The register labels describe computational basis strings. Write

```math
A=\bigoplus_{v\in V} a_v,\qquad Z=\bigoplus_{v\in V} z_v .
```

The target is the diagonal unitary

```math
U\lvert (a_v,z_v)_{v\in V}\rangle
=(-1)^{Z[A]}\lvert (a_v,z_v)_{v\in V}\rangle .
```

On a superposition, the signs change relative phases. A classical evaluation of the lookup on basis inputs would give an output bit and dephase arbitrary inputs. The quantum channel must act on the original register at each module and preserve its correlations with any untouched reference.

## Resources and error

| Item | Convention |
| --- | --- |
| Initial network resources | Edge $`e`$ has at most $`b_e`$ ideal Bell pairs. Each $`b_e`$ is a nonnegative integer fixed before the run. |
| Local operations | Local gates, preparation, measurements and classical processing, with ancillary quantum storage. |
| Communication | Classical messages and shared randomness. The interactive construction sends messages between adjacent modules. |
| Accuracy | Half the diamond norm between the unconditional implemented channel and $`\mathrm{Ad}_U`$, where $`\mathrm{Ad}_U(\rho)=U\rho U^\dagger`$. |

For a channel $`\mathcal E`$ the accuracy criterion is

```math
\delta(\mathcal E,U)=\frac12\left\|\mathcal E-\mathrm{Ad}_U\right\|_\diamond .
```

The diamond norm includes arbitrary reference inputs. A protocol's classical outcomes are used for its feedforward and discarded for this comparison. Each charged Bell pair is a separate shared input resource. The budget is a per-run cap, including any pairs used before the first message.

Each local sign $`(-1)^{z_v[A]}`$ is implemented from the explicit table register. A reversible binary decoder can traverse the table with $`O(D)`$ local Toffoli and controlled-Z gates and $`O(k)`$ clean flags. The routing also uses temporary address copies. This resource law permits arbitrary local storage and does not charge classical latency against the Bell-pair budget. It gives no operation for loading a classical database into coherent quantum inputs.

## Cuts and rounds

Deleting edge $`e`$ partitions the tree into two sides. For a converse, give the modules within each side joint control. The sole initial entanglement across that cut then consists of the $`b_e`$ edge Bell pairs. Within either side, the aggregated address and data strings are surjective XORs, each with equal-size preimages. This makes the cut reduction independent of how many modules lie on either side.

The [one-exchange model](simultaneous-exchange.md) restricts classical communication across a cut to a single simultaneous exchange. Each side chooses its outgoing message from its own pre-exchange instrument without seeing the other message. Each can finish with arbitrary local processing after receipt. The stronger entanglement cost follows for a cut with this communication restriction. The [interactive tree result](interactive-tree.md) permits feedback across the cut.

## Relation to prior work

The Boolean function $`(A,Z)\mapsto(-1)^{Z[A]}`$ is the usual address function. Its Walsh expansion underlies the cut calculation, and nonlocal-gate operator Schmidt rank gives the exact-simulation lower bound. The results here concern the optimum deterministic channel error at each hard link budget, a protocol attaining it on every tree, and the same gate's cost under a one-exchange constraint. [Sanyal, Fourier Sparsity and Dimension](https://doi.org/10.4086/toc.2019.v015a011). [Stahlke and Griffiths, Entanglement requirements for implementing bipartite unitary operations](https://doi.org/10.1103/PhysRevA.84.032316).

Aljuaydi and coauthors report a general process-fidelity converse from the ordered operator-Schmidt spectrum and give a separate flat-spectrum example for dual-unitary brickwork circuits. Our finite-error proof uses the same cut converse. Its matching upper bound comes from the addressed-phase compiler and controls diamond distance for all inputs. The comparison here is based on the publisher's early-posting abstract. [Aljuaydi et al., Entanglement Lower Bounds and Reliability in Distributed Quantum Computing](https://opg.optica.org/josab/upcoming_pdf.cfm?id=618830).

For general bipartite gates, exact Clifford protocols can attain the operator-Schmidt lower bound with constant qubit overhead, and Clifford+T protocols have a T-count-dependent bound. The compiler here exploits the address structure and uses temporary address registers. [Matsui et al., Reducing the Entanglement Cost of Distributed Bipartite Quantum Computation with Constant Qubit Overhead](https://arxiv.org/abs/2609.39865).

Matsui and coauthors study the entanglement cost of synthesis for a chosen gate decomposition. Distributed circuit-packing work additionally accounts for the placement of gates and constraints of the physical network. Here the gate and placement of its inputs are fixed, allowing a converse against arbitrary interactive strategies on that network. [Andrés-Martínez et al., Distributing Circuits over Heterogeneous, Modular Quantum Computing Network Architectures](https://arxiv.org/abs/2305.14148).
