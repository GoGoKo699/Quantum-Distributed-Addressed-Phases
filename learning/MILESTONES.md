# Distributed addressed phases in 30 milestones

The 12 background milestones connect the input registers, classical messages, and channel tests. The 18 narrative milestones follow the cut converse, the all-budget construction, and the exact and fixed-error simultaneous-exchange bounds. The [Watrous bridge](WATROUS_BRIDGE.md) identifies the relevant sections of the educational anchor and introduces the two-module example.

| Phase | Milestones | What they connect |
| --- | --- | --- |
| Background | [M01–M04](#m01-address-and-data-registers) | Local inputs, references and measurement records |
| Background | [M05–M08](#m05-bell-pairs-across-a-cut) | Entanglement across a cut, Choi states and channel error |
| Background | [M09–M12](#m09-walsh-characters) | Finite binary algebra and the complete simulation task |
| Narrative | [M13–M16](#m13-aggregating-each-side-of-a-cut) | Walsh spectrum and the Bell-budget converse |
| Narrative | [M17–M21](#m17-a-bell-assisted-label-copy) | Coherent address routing and local signs |
| Narrative | [M22–M26](#m22-splitting-the-address-by-budget) | Attaining the optimal deterministic error at every budget |
| Narrative | [M27–M30](#m27-the-timing-of-a-simultaneous-exchange) | The pre-exchange state, phase-column count, and fixed-error cost |

## Background and preliminaries

### M01 Address and data registers

**Central question.** What does each processor hold when a run begins?

**Understanding target.** Identify $`k`$ native address qubits and a table of $`2^k`$ native data qubits at each module. Read a string $`z_v`$ as a computational-basis label for the entire table.

**Prerequisites.** None within this map.

**Conceptual connection.** Treating the table as a full register specifies what can be in superposition and which wires must return at the end.

**Sources.** [Model](../science/model.md) and [Watrous bridge](WATROUS_BRIDGE.md#reading-the-anchor).

### M02 From a basis sign to a quantum gate

**Central question.** What can a diagonal gate change when it preserves all basis labels?

**Understanding target.** Use linearity to determine the output on a superposition from its basis signs. Explain how opposite signs on two components change an interference measurement.

**Prerequisites.** [M01](#m01-address-and-data-registers).

**Conceptual connection.** A classical lookup can reproduce every basis sign and still fail to implement the coherent channel.

**Sources.** [Model](../science/model.md) and [two-module example](WATROUS_BRIDGE.md#one-address-bit-on-two-modules).

### M03 References and local reductions

**Central question.** What must the implementation preserve about a qubit entangled with another system?

**Understanding target.** Interpret the target as $`\mathcal U\otimes\operatorname{id}_R`$ on data and reference together. Use a partial trace to describe the state available at one location without access to the other registers.

**Prerequisites.** [M01](#m01-address-and-data-registers), [M02](#m02-from-a-basis-sign-to-a-quantum-gate).

**Conceptual connection.** Two processes can agree on the input register's basis probabilities and differ in its correlations with a reference.

**Sources.** [Model](../science/model.md) and [Watrous, Sections 2.1.2–2.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M04 Branches of a channel

**Central question.** How does an instrument with classical outcomes act on a quantum input?

**Understanding target.** Associate each fine-grained outcome with an operator and use the completeness relation to recover a deterministic channel when all outcomes are included.

**Prerequisites.** [M03](#m03-references-and-local-reductions).

**Conceptual connection.** In one use of an instrument, its outcome can direct a correction. Across all uses, the unconditional channel determines the simulation error.

**Sources.** [Watrous, Sections 2.2–2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [interactive tree protocol](../science/interactive-tree.md).

### M05 Bell pairs across a cut

**Central question.** Which link resources can generate entanglement across a partition of the modules?

**Understanding target.** Identify the Bell pairs bisected by the partition and compute their product Schmidt rank. Treat all remaining Bell pairs as local resources when the modules on each side may cooperate.

**Prerequisites.** [M01](#m01-address-and-data-registers), [M03](#m03-references-and-local-reductions).

**Conceptual connection.** Deleting an edge of a tree gives a cut with exactly one charged link, so a constraint on that link bounds the entire protocol.

**Sources.** [Model](../science/model.md) and [Watrous, Sections 6.1.1–6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf).

### M06 Local operations and Schmidt number

**Central question.** What remains bounded after measurements, classical feedback and discarded outcomes?

**Understanding target.** Explain why a product operator preserves an upper bound on Schmidt rank on each pure branch. Interpret averaging and tracing local registers as producing a mixed state of bounded Schmidt number.

**Prerequisites.** [M04](#m04-branches-of-a-channel), [M05](#m05-bell-pairs-across-a-cut).

**Conceptual connection.** Local resources, communication and branch-dependent corrections cannot increase the cross-cut rank cap beyond the initial shared Bell stock.

**Sources.** [Cut converse](../science/interactive-tree.md) and [Watrous, Section 6.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf).

### M07 A Choi probe with local reference pairs

**Central question.** How can a single input state record the gate's action on all matrix elements?

**Understanding target.** Form a maximally entangled state between each module's input and a local reference. Apply the gate to the input halves and recognize the resulting normalized Choi state.

**Prerequisites.** [M03](#m03-references-and-local-reductions), [M05](#m05-bell-pairs-across-a-cut).

**Conceptual connection.** Local input-reference pairs provide a channel probe without supplying initial entanglement across a module cut.

**Sources.** [Watrous, Section 2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [cut converse](../science/interactive-tree.md).

### M08 Distinguishing channels with a reference

**Central question.** What can a failed state test certify about a channel simulation?

**Understanding target.** Explain why the difference between two channels on one referenced probe lower-bounds their half-diamond distance. Read a difference of outcome probabilities as a lower bound on half trace distance.

**Prerequisites.** [M04](#m04-branches-of-a-channel), [M07](#m07-a-choi-probe-with-local-reference-pairs).

**Conceptual connection.** Projecting onto the ideal Choi vector turns a cap on its overlap into an operational lower bound on channel error.

**Sources.** [Watrous, Sections 3.1.1 and 3.3.2–3.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) and [Watrous bridge](WATROUS_BRIDGE.md#crossing-the-cut-in-the-proof).

### M09 Walsh characters

**Central question.** How does XOR become multiplication in a sign-valued representation?

**Understanding target.** Use $`\chi_p(a)=(-1)^{p\cdot a}`$ and its character law. Verify that two different characters have zero mean product under the uniform distribution.

**Prerequisites.** [M01](#m01-address-and-data-registers).

**Conceptual connection.** The character law allows a sign depending on a global XOR to be expanded in products of signs local to opposite sides of a cut.

**Sources.** [Cut converse](../science/interactive-tree.md).

### M10 Randomness and equivalent Kraus representations

**Central question.** Can the same implementation channel have two descriptions with different individual branch operators?

**Understanding target.** Relate the probability of a random branch to the square of its Kraus amplitude. Use a unitary change of Kraus basis to combine branch amplitudes without changing the channel sum.

**Prerequisites.** [M04](#m04-branches-of-a-channel), [M09](#m09-walsh-characters).

**Conceptual connection.** A term proportional to the target operator in a new Kraus representation certifies a mixture weight even if the protocol has no corresponding classical flag.

**Sources.** [Watrous, Section 2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [interactive tree protocol](../science/interactive-tree.md).

### M11 Message order and local feed-forward

**Central question.** What changes when messages are exchanged simultaneously?

**Understanding target.** Distinguish making a decision after receiving a message from choosing both outgoing messages in advance. Track which corrections a party can apply after the exchange.

**Prerequisites.** [M04](#m04-branches-of-a-channel), [M05](#m05-bell-pairs-across-a-cut).

**Conceptual connection.** The simultaneous model constrains causal dependence even when the messages themselves may be arbitrarily long.

**Sources.** [Model](../science/model.md) and [simultaneous exchange](../science/simultaneous-exchange.md).

### M12 The simulation task and its resources

**Central question.** What does a claimed optimum need to hold fixed?

**Understanding target.** State the target channel, native-output requirement, charged Bell budgets, message schedule and half-diamond error convention. Explain what deterministic implementation means when measurements and randomness are used.

**Prerequisites.** [M02](#m02-from-a-basis-sign-to-a-quantum-gate), [M06](#m06-local-operations-and-schmidt-number), [M08](#m08-distinguishing-channels-with-a-reference), [M10](#m10-randomness-and-equivalent-kraus-representations), [M11](#m11-message-order-and-local-feed-forward).

**Conceptual connection.** The cost of implementing the channel and the work of processing a local explicit table answer different resource questions.

**Sources.** [Model](../science/model.md).

## Narrative and innovation

### M13 Aggregating each side of a cut

**Central question.** What information about the computational labels on each side enters the phase?

**Understanding target.** XOR all addresses and all tables on each side separately. Combine the two summaries to recover the address and table used by the gate. Explain why every summary has equally many preimages.

**Prerequisites.** [M01](#m01-address-and-data-registers), [M09](#m09-walsh-characters), [M12](#m12-the-simulation-task-and-its-resources).

**Conceptual connection.** Equal preimage counts let a uniform Choi probe of the full module registers realize uniform summaries without changing the implementation problem.

**Sources.** [Cut converse](../science/interactive-tree.md).

### M14 Fourier coefficients of the addressed sign

**Central question.** Which characters survive the Fourier transform of $`(-1)^{Z[A]}`$?

**Understanding target.** For fixed address $`a`$, average over the complete data table. A coefficient survives only when the table character selects precisely that entry. Evaluate its remaining address character and magnitude.

**Prerequisites.** [M09](#m09-walsh-characters), [M13](#m13-aggregating-each-side-of-a-cut).

**Conceptual connection.** The address function has many input bits yet only $`4^k`$ nonzero Fourier coefficients, all of magnitude $`2^{-k}`$.

**Sources.** [Cut converse](../science/interactive-tree.md).

### M15 A flat Schmidt spectrum

**Central question.** Why do the surviving Fourier coefficients become Schmidt coefficients?

**Understanding target.** Turn the local summary characters into vectors by multiplying the amplitudes of the local Choi probe. Use their orthogonality and normalize the resulting decomposition.

**Prerequisites.** [M07](#m07-a-choi-probe-with-local-reference-pairs), [M13](#m13-aggregating-each-side-of-a-cut), [M14](#m14-fourier-coefficients-of-the-addressed-sign).

**Conceptual connection.** The phase table supplies $`4^k`$ equal squared Schmidt coefficients across every nontrivial module cut.

**Sources.** [Cut converse](../science/interactive-tree.md).

### M16 Turning the Schmidt cap into an error bound

**Central question.** How closely can a limited-entanglement protocol imitate the flat Choi vector?

**Understanding target.** Relate the greatest squared overlap of a rank-limited state to the sum of the largest target Schmidt weights. Apply this cap to every conditional pure state and then to the averaged output.

**Prerequisites.** [M06](#m06-local-operations-and-schmidt-number), [M08](#m08-distinguishing-channels-with-a-reference), [M15](#m15-a-flat-schmidt-spectrum).

**Conceptual connection.** Every edge independently supplies a lower bound on the attainable error, and the smallest Bell stock gives the strongest one.

**Sources.** [Cut converse](../science/interactive-tree.md).

### M17 A Bell-assisted label copy

**Central question.** How can the receiver acquire a coherent computational label from a distant qubit?

**Understanding target.** Follow a CNOT into the sender's Bell half, its computational-basis measurement, and an outcome-dependent $`X`$ correction at the receiver. Track both amplitudes and confirm that the outcome is uniform.

**Prerequisites.** [M02](#m02-from-a-basis-sign-to-a-quantum-gate), [M03](#m03-references-and-local-reductions), [M04](#m04-branches-of-a-channel).

**Conceptual connection.** This primitive distributes a coherent control label for use in the tree while consuming one Bell pair.

**Sources.** [Interactive tree protocol](../science/interactive-tree.md) and [Watrous bridge](WATROUS_BRIDGE.md#one-address-bit-on-two-modules).

### M18 Erasing a temporary label copy

**Central question.** How can the receiver discard its copy without leaving a record of the computational label?

**Understanding target.** Compute the phase induced by an $`X`$-basis measurement of the copy. Show that a $`Z`$ correction on the original removes that phase and preserves correlations with other registers.

**Prerequisites.** [M17](#m17-a-bell-assisted-label-copy).

**Conceptual connection.** The erasure step uses a classical outcome and local correction. It allows the protocol to recycle temporary label registers without additional Bell pairs.

**Sources.** [Interactive tree protocol](../science/interactive-tree.md).

### M19 Gathering the global address

**Central question.** How does the root compute a global XOR without learning the input addresses as classical strings?

**Understanding target.** Follow a subtree XOR from its children to its accumulator and then to its parent. Account for one coherent label copy per address bit on each upward edge.

**Prerequisites.** [M13](#m13-aggregating-each-side-of-a-cut), [M17](#m17-a-bell-assisted-label-copy).

**Conceptual connection.** An upward pass computes the XOR on a coherent workspace and supplies the root control for later phases.

**Sources.** [Interactive tree protocol](../science/interactive-tree.md).

### M20 Broadcasting the address and applying local signs

**Central question.** Why is one local phase at each module sufficient once the global address is available?

**Understanding target.** Follow a root address copy down the tree and multiply the signs $`(-1)^{z_v[A]}`$ from each module. Recover the target phase from this product.

**Prerequisites.** [M02](#m02-from-a-basis-sign-to-a-quantum-gate), [M17](#m17-a-bell-assisted-label-copy), [M19](#m19-gathering-the-global-address).

**Conceptual connection.** Only address labels travel through the Bell-assisted operations. The data tables remain at their original modules.

**Sources.** [Interactive tree protocol](../science/interactive-tree.md).

### M21 Uncomputing the routing workspace

**Central question.** Which temporary labels must be erased first to preserve the gate on the native input?

**Understanding target.** Reverse the broadcast, erase its copies, and then reverse the gathering XORs and erase their copies. Explain why the address registers and the local data tables remain in their initial locations with the intended phases.

**Prerequisites.** [M18](#m18-erasing-a-temporary-label-copy), [M19](#m19-gathering-the-global-address), [M20](#m20-broadcasting-the-address-and-applying-local-signs).

**Conceptual connection.** The complete up-and-down routing uses two Bell pairs per edge per coherent address bit and returns all routing workspace independent of the data.

**Sources.** [Interactive tree protocol](../science/interactive-tree.md).

### M22 Splitting the address by budget

**Central question.** How can a protocol use an odd Bell budget without treating the last pair as wasted?

**Understanding target.** Decompose the capped bottleneck budget as $`b=2\ell+j`$ with $`j\in\{0,1\}`$. Assign $`\ell`$ bits coherent routing, $`j`$ bits gathered parity measurement, and the remaining $`k-\ell-j`$ bits random slice treatment.

**Prerequisites.** [M16](#m16-turning-the-schmidt-cap-into-an-error-bound), [M21](#m21-uncomputing-the-routing-workspace).

**Conceptual connection.** Each type of address bit consumes its own Bell cost and contributes differently to the weight of the target channel.

**Sources.** [Budgeted interactive construction](../science/interactive-tree.md).

### M23 Measuring global parity

**Central question.** What coherence survives a measurement of the XOR of one address bit across the modules?

**Understanding target.** Recognize that a parity measurement preserves coherence within each parity sector and erases coherence between sectors when its record is omitted. Express this dephasing as an equal mixture of the identity and conjugation by the product address $`Z`$.

**Prerequisites.** [M04](#m04-branches-of-a-channel), [M19](#m19-gathering-the-global-address), [M22](#m22-splitting-the-address-by-budget).

**Conceptual connection.** One upward copy per edge resolves the odd-budget bit for classical control and costs half the target weight associated with that bit.

**Sources.** [Budgeted interactive construction](../science/interactive-tree.md).

### M24 Randomized slices and characters

**Central question.** How can the simulation use high address bits that never leave their home modules?

**Understanding target.** Combine a guessed high slice with a random Walsh character. Explain how each module evaluates the slice locally using the available address bits and contributes its part of the character phase.

**Prerequisites.** [M09](#m09-walsh-characters), [M20](#m20-broadcasting-the-address-and-applying-local-signs), [M22](#m22-splitting-the-address-by-budget).

**Conceptual connection.** Character orthogonality selects the correct slice in a signed sum of the implemented branch operators.

**Sources.** [Budgeted interactive construction](../science/interactive-tree.md).

### M25 Extracting the target channel weight

**Central question.** How does a signed sum of branch operators constrain the error of their mixture?

**Understanding target.** Normalize the signed coefficient row as a Kraus change of basis and compute the target component's squared amplitude. Include the identity term of odd-bit dephasing when required.

**Prerequisites.** [M10](#m10-randomness-and-equivalent-kraus-representations), [M23](#m23-measuring-global-parity), [M24](#m24-randomized-slices-and-characters).

**Conceptual connection.** An explicit target component of weight $`2^{b-2k}`$ bounds the unconditional half-diamond error by $`1-2^{b-2k}`$.

**Sources.** [Budgeted interactive construction](../science/interactive-tree.md) and [Watrous bridge](WATROUS_BRIDGE.md#crossing-the-cut-in-the-proof).

### M26 An attained error at every tree budget

**Central question.** Why is the budget law exact over the entire range?

**Understanding target.** Compare the achievable error with the cut converse. Check $`k=1`$ at budgets zero, one and two, and explain when increasing the budget of a nonbottleneck edge can affect the minimum.

**Prerequisites.** [M16](#m16-turning-the-schmidt-cap-into-an-error-bound), [M22](#m22-splitting-the-address-by-budget), [M25](#m25-extracting-the-target-channel-weight).

**Conceptual connection.** The same integer bottleneck budget controls both arguments, giving one optimal deterministic channel error at every budget.

**Sources.** [Interactive frontier](../science/interactive-tree.md) and [two-module example](WATROUS_BRIDGE.md#one-address-bit-on-two-modules).

### M27 The timing of a simultaneous exchange

**Central question.** What information can a party hold before any message arrives?

**Understanding target.** Model the two sides' pre-exchange actions as local instruments using shared Bell pairs. Explain why Bob's pre-exchange reduced state is independent of Alice's input. On the reference-pair test, relate the ideal phase on the inputs to a diagonal operator on Bob's reference after undoing his final correction.

**Prerequisites.** [M04](#m04-branches-of-a-channel), [M07](#m07-a-choi-probe-with-local-reference-pairs), [M11](#m11-message-order-and-local-feed-forward), [M12](#m12-the-simulation-task-and-its-resources).

**Conceptual connection.** Grouping the modules on each side of a cut relaxes the local operations while preserving the required timing of messages across the cut.

**Sources.** [Simultaneous model](../science/simultaneous-exchange.md).

### M28 Exact cost from phase columns

**Central question.** Why does exact implementation charge for distinct phase columns?

**Understanding target.** Explain why an exact simulation leaves Bob's pre-exchange state invariant under all relative phase rows. For equal column addresses, identify the two tables that differ by a constant bit. For different addresses, use Alice's table to distinguish selected entries. Count $`2^{k+2^k-1}`$ inequivalent columns.

**Prerequisites.** [M06](#m06-local-operations-and-schmidt-number), [M13](#m13-aggregating-each-side-of-a-cut), [M27](#m27-the-timing-of-a-simultaneous-exchange).

**Conceptual connection.** Invariance forces the reference labels for inequivalent columns into separate blocks. Their uniform weights conditional on the message yield an entropy lower bound of $`k+2^k-1`$ ebits.

**Sources.** [Simultaneous-exchange converse](../science/simultaneous-exchange.md).

### M29 A fixed-error cost from decoding table bits

**Central question.** How much of the simultaneous lower bound survives a small nonzero error?

**Understanding target.** In the restricted gate with phase $`(-1)^{w_x}`$, use the row comparison to identify the relative table bits $`w_i\oplus w_0`$. Explain how approximate invariance makes each bit recoverable, on average, from the other side's half of the Bell resource and Bob's message. Relate this decoding guarantee to a lower bound on shared entanglement.

**Prerequisites.** [M08](#m08-distinguishing-channels-with-a-reference), [M27](#m27-the-timing-of-a-simultaneous-exchange), [M28](#m28-exact-cost-from-phase-columns).

**Conceptual connection.** A fixed-input overlap estimate controls the decoding error without a factor that grows with the full input dimension. Information bounds then force order $`2^k`$ Bell pairs at sufficiently small fixed half-diamond error.

**Sources.** [Fixed-error lower bound](../science/simultaneous-exchange.md), [Watrous, Sections 3.1–3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), and [Watrous, Sections 5.1–5.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf).

### M30 Choosing a compiler by error and message order

**Central question.** What does the compiler let a network designer trade, and which models require a separate analysis?

**Understanding target.** State the exact interactive tree frontier and compare its zero-error cost and small-error costs with the corresponding simultaneous lower bounds. Specify the native quantum inputs, Bell charge, local gate work, and reference-sensitive error convention.

**Prerequisites.** [M12](#m12-the-simulation-task-and-its-resources), [M26](#m26-an-attained-error-at-every-tree-budget), [M29](#m29-a-fixed-error-cost-from-decoding-table-bits).

**Conceptual connection.** The same gate has an exponentially larger Bell requirement with simultaneous messages, even at sufficiently small fixed error. The tree theorem attains its full frontier. The simultaneous bounds give necessary resources, and the routing argument uses a tree.

**Sources.** [Model](../science/model.md), [interactive frontier](../science/interactive-tree.md), and [simultaneous exchange](../science/simultaneous-exchange.md).
