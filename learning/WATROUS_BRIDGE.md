# From Watrous to distributed addressed phases

Two quantum processors each have an address register and a table of data qubits. Their gate uses the XOR of the addresses to select a data qubit at each processor and applies a sign from the XOR of the selected bits. The address and data qubits remain at their original processors and may be entangled with a reference. The question is how much Bell entanglement the processors must share to realize the resulting coherent gate.

The educational anchor is **John Watrous, *The Theory of Quantum Information***, published by Cambridge University Press in 2018. The sections below refer to the author's [2018 manuscript](https://jhwatrous.github.io/books-and-courses.html#the-theory-of-quantum-information). Start with the relevant section and the corresponding stop in the [30-milestone map](MILESTONES.md). The [model](../science/model.md) gives the exact claims and assumptions.

## Reading the anchor

| Reading | How it enters the project |
| --- | --- |
| [Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) on quantum states, reductions and purifications | Identify native input registers, the external reference and the local halves of a charged Bell pair. |
| [Sections 2.2.1–2.2.2 and 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) on channels, representations and measurement | Translate measured branches into Kraus operators. Use the Choi matrix to certify branch factorization and the unitary freedom of Kraus representations to analyze a mixture. |
| [Sections 3.1.1, 3.2.2–3.2.3 and 3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) on discrimination and fidelity | Use a target projector to bound channel error, and convert small reference coherences into bounds on binary discrimination error. |
| [Sections 5.1.1–5.1.2 and 5.2.1–5.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) on classical and quantum entropy | Interpret what the exact phase-column blocks reveal and bound how many relative table bits the shared resource can encode. |
| [Sections 6.1.1–6.1.2 and 6.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) on separability, LOCC and teleportation | Track local maps and classical messages on a cut, and understand Bell-assisted feed-forward. |

Watrous supplies the general quantum-information tools. The project's scientific pages develop the addressed gate's Walsh expansion and flat Choi spectrum, which give an error converse that the interactive compiler attains at each integer Bell budget. The simultaneous proof instead counts distinguishable phase columns and uses the decodability of table bits to retain a lower bound at nonzero error.

## Notation at a glance

| Source concept | Project object |
| --- | --- |
| A register and its purifying reference | Each module holds $`k`$ address qubits and $`D=2^k`$ data qubits. The reference is outside the implementation's operations. |
| The channel associated with an isometry | $`\mathcal U(\rho)=U\rho U^\dagger`$, where $`U`$ applies the addressed sign to each computational-basis vector. |
| Choi matrix $`J(\Phi)`$ from the unnormalized maximally entangled vector | A Choi state from normalized, maximally entangled input-reference pairs. The normalization makes target overlap a probability. |
| The completely bounded trace norm | $`\lVert\Phi-\mathcal U\rVert_\diamond`$. The reported error is half of this norm. |
| A local classical outcome selecting a later operation | A transcript in interactive LOCC, or one of the two messages determined before the simultaneous exchange. |
| A pure state's Schmidt rank | The number of nonzero terms in a bipartite Schmidt decomposition. For mixed outputs, the Schmidt-number bound means that the state admits an ensemble of pure states each with rank at most the bound. |

## One address bit on two modules

Write the address bits as $`a_1,a_2`$ and the two data bits at each module as $`z_i[0],z_i[1]`$. Take the basis input with $`a_1=0`$, $`a_2=1`$, $`z_1=(0,1)`$ and $`z_2=(0,0)`$. Both modules select entry 1 because $`a_1\oplus a_2=1`$. The selected data XOR is 1, so the sign is negative. Change only $`a_2`$ to 0 and the sign becomes positive.

A superposition of the two address inputs therefore changes its relative phase. Measuring each address and then consulting the two tables would erase the coherence needed to distinguish the output from the input by interference. The project instead uses a Bell pair to make a temporary computational-label copy of a qubit. If the source is part of $`\sum_{x=0}^1 |x\rangle|\eta_x\rangle`$, the corrected copy changes this to $`\sum_x |x\rangle|x\rangle|\eta_x\rangle`$. The vectors $`|\eta_x\rangle`$ can contain arbitrary data and references. The resulting two-qubit register is an encoding of the source into correlated labels. Its receiving half alone has lost the off-diagonal terms of the source.

With two Bell pairs, use the first for gathering the XOR at one module and the second for broadcasting the coherent global address back. Apply each local sign and erase both temporary copies with phase corrections. With one Bell pair, gather and measure the global XOR. The optimal simulation dephases between the two XOR sectors and attains half-diamond error $`1/2`$. With zero Bell pairs, a random address slice and sign character attain error $`3/4`$. These three values are the $`k=1`$ case of the general [interactive frontier](../science/interactive-tree.md).

## Crossing the cut in the proof

On a tree, removing an edge divides the modules into two groups. The lower bound lets each group act jointly and gives every input a maximally entangled local reference. The probe thus starts separable across the cut, apart from the charged Bell stock. After the target gate, Fourier characters of each group's XOR summary label orthogonal vectors. The target has $`4^k`$ equal squared Schmidt coefficients. A protocol with $`b_e`$ Bell pairs can only make an output of Schmidt number at most $`2^{b_e}`$. Its overlap with the target projector is therefore at most $`\min(1,2^{b_e-2k})`$.

The matching upper bound is a statement about the whole channel. A change of Kraus representation isolates the ideal channel with weight $`2^{b-2k}`$, where $`b=\min(2k,\min_e b_e)`$. The remaining weight bounds the half-diamond error. This reasoning averages all implemented outcomes. It does not require an experimental flag identifying the ideal component.

## Changing the order of classical messages

In the [simultaneous model](../science/simultaneous-exchange.md), each module group must finish its first local instrument before learning the other group's message. On a referenced test input, exactly reproducing the ideal pure state leaves all retained environments uncorrelated with that state. Undoing Bob's correction puts the ideal phases on his reference, while tracing out Alice makes the actual pre-exchange state independent of her input. The proof combines these facts to force blocks between nonproportional phase columns to vanish. The entropy of the resulting uniform column label gives the exact Bell lower bound across the cut.

At nonzero channel error, a restricted gate test lets Alice's address select a sign from Bob's table. Its pairwise phase tests show that the relative bit $`w_i\oplus w_0`$ can be guessed with low average error from Alice's share of the initial resource and Bob's message. The same test makes that message nearly independent of the uniform relative bits. Applying a binary error bound and the entropy bound on the resource yields a Bell cost proportional to the table length at sufficiently small fixed error. The [simultaneous proof](../science/simultaneous-exchange.md) gives the constants and the allowed error range.
