"""Exact small-instance checks of the interactive addressed-phase compiler."""

from itertools import product


def parity(value):
    return value.bit_count() % 2


def character(mask, value):
    return 1 - 2 * parity(mask & value)


def bell_copy(source, outcome):
    """Return the corrected target bit in a normalized cobit branch."""
    matching_halves = [half for half in (0, 1) if half ^ source == outcome]
    assert len(matching_halves) == 1
    return matching_halves[0] ^ outcome


def path_branch(addresses, tables, bell_outcomes, x_outcomes, measure_address):
    """Reduce one k=1 branch on the three-module path 0--1--2.

    Registers carry their actual basis value and the linear mask used for
    feedforward. The returned phase omits only the common positive branch
    amplitude, with one factor of 1/sqrt(2) per Bell or X measurement.
    """
    parents = (None, 0, 1)
    accumulators = [(addresses >> v & 1, 1 << v) for v in range(3)]
    gathered = []
    delivered = [None, None, None]
    bell_outcomes = iter(bell_outcomes)

    for child in (2, 1):
        parent = parents[child]
        child_bit, child_mask = accumulators[child]
        received = bell_copy(child_bit, next(bell_outcomes))
        gathered.append((received, child_mask))
        parent_bit, parent_mask = accumulators[parent]
        accumulators[parent] = received ^ parent_bit, child_mask ^ parent_mask

    measured = None
    if measure_address:
        measured, _ = accumulators.pop(0)
        for v in range(3):
            delivered[v] = measured, 0
        scratch = accumulators + gathered
    else:
        delivered[0] = accumulators[0]
        for child in (1, 2):
            source_bit, source_mask = delivered[parents[child]]
            received = bell_copy(source_bit, next(bell_outcomes))
            delivered[child] = received, source_mask
        scratch = accumulators + gathered + delivered[1:]

    assert next(bell_outcomes, None) is None
    target_values = [tables[v] >> delivered[v][0] & 1 for v in range(3)]
    target_phase = sum(target_values) % 2

    measurement_phase = 0
    correction_mask = 0
    for outcome, (bit, mask) in zip(x_outcomes, scratch, strict=True):
        measurement_phase ^= outcome & bit
        if outcome:
            correction_mask ^= mask
    overall_phase = target_phase ^ measurement_phase ^ parity(addresses & correction_mask)
    return 1 - 2 * overall_phase, measured


def verify_path_branches():
    for source, outcome in product((0, 1), repeat=2):
        assert bell_copy(source, outcome) == source

    count = 0
    for measure_address in (False, True):
        bell_count, x_count = (2, 4) if measure_address else (4, 7)
        for addresses in range(8):
            address = parity(addresses)
            expected_measurement = address if measure_address else None

            for outcomes in product((0, 1), repeat=bell_count + x_count):
                tables = (1, 2, 1)
                phase = character(1 << address, tables[0] ^ tables[1] ^ tables[2])
                assert path_branch(
                    addresses, tables, outcomes[:bell_count], outcomes[bell_count:], measure_address
                ) == (phase, expected_measurement)
                count += 1

            for tables in product(range(4), repeat=3):
                phase = character(1 << address, tables[0] ^ tables[1] ^ tables[2])
                assert path_branch(
                    addresses, tables, (0,) * bell_count, (0,) * x_count, measure_address
                ) == (phase, expected_measurement)
                count += 1
    return count


def walsh_transform(values):
    """Return unnormalized Walsh coefficients using integer arithmetic."""
    spectrum = values.copy()
    step = 1
    while step < len(spectrum):
        for start in range(0, len(spectrum), 2 * step):
            for left in range(start, start + step):
                right = left + step
                a, b = spectrum[left], spectrum[right]
                spectrum[left] = a + b
                spectrum[right] = a - b
        step *= 2
    return spectrum


def verify_frontier(k):
    address_count = 1 << k
    labels = list(product(range(1 << address_count), range(address_count)))
    target = [character(1 << address, table) for table, address in labels]
    expected = [0] * len(labels)
    for address, t in product(range(address_count), repeat=2):
        expected[(1 << address) * address_count + t] = (
            len(labels) // address_count * character(t, address)
        )
    assert walsh_transform(target) == expected

    for budget in range(2 * k + 1):
        low_count, middle_count = divmod(budget, 2)
        coherent_and_measured_count = low_count + middle_count
        high_values = 1 << (k - coherent_and_measured_count)
        lower_mask = (1 << coherent_and_measured_count) - 1
        expansion = [0] * len(labels)
        overlap_numerator = 0

        for fixed_high, t in product(range(high_values), repeat=2):
            slice_diagonal = []
            for table, address in labels:
                selected = fixed_high << coherent_and_measured_count | address & lower_mask
                high = address >> coherent_and_measured_count
                slice_diagonal.append(character(1 << selected, table) * character(t, high))
            coefficient = character(t, fixed_high)
            for index, value in enumerate(slice_diagonal):
                expansion[index] += coefficient * value

            for middle_character in range(1 << middle_count):
                trace = sum(
                    u * v * character(middle_character, address >> low_count)
                    for u, v, (_, address) in zip(target, slice_diagonal, labels, strict=True)
                )
                overlap_numerator += trace**2

        assert expansion == [high_values * phase for phase in target]
        # The expected squared overlap is 1 / (high_values**2 * 2**middle_count).
        # This factor also normalizes the equally weighted channels in the sum.
        assert overlap_numerator == len(labels) ** 2


if __name__ == "__main__":
    branch_count = verify_path_branches()
    print(f"Three-module path: {branch_count} coherent or measured branch checks passed.")
    for k in (1, 2, 3):
        verify_frontier(k)
        print(f"k={k}: Walsh spectrum and all {2 * k + 1} Bell budgets passed.")
