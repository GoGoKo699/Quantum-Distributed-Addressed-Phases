"""Verify finite cases of the constructive one-exchange addressed-phase circuit."""

from itertools import product


def sign(bit):
    return 1 - 2 * (bit % 2)


def corrected_cz_numerator(control, target, z_outcome, x_outcome):
    """Compute twice the corrected branch amplitude in the basis of the flags."""
    amplitude = 0
    for bell_bit in (0, 1):
        if control ^ bell_bit == z_outcome:
            amplitude += sign(bell_bit * target) * sign(bell_bit * x_outcome)
    return amplitude * sign(x_outcome * control) * sign(z_outcome * target)


def verify_remote_cz():
    for control, target, z_outcome, x_outcome in product((0, 1), repeat=4):
        expected = sign(control * target) * sign(z_outcome * x_outcome)
        assert corrected_cz_numerator(control, target, z_outcome, x_outcome) == expected


def xor_relabel(table, address):
    """Execute the local conditional swaps for the supplied basis address."""
    relabeled = list(table)
    bit = 1
    while bit < len(table):
        if address & bit:
            for index in range(len(table)):
                if not index & bit:
                    partner = index | bit
                    relabeled[index], relabeled[partner] = relabeled[partner], relabeled[index]
        bit <<= 1
    return tuple(relabeled)


def lookup_terms(table, address):
    """Return the remote CZ flag pairs with the entry-zero phase factored out."""
    return [(int(address == i), table[i] ^ table[0]) for i in range(1, len(table))]


def verify_relabeling(k):
    size = 1 << k
    cases = 0
    for table in product((0, 1), repeat=size):
        for local_address in range(size):
            relabeled = xor_relabel(table, local_address)
            assert xor_relabel(relabeled, local_address) == table
            for remote_address in range(size):
                lookup = relabeled[0] ^ (sum(q * r for q, r in lookup_terms(relabeled, remote_address)) % 2)
                assert lookup == relabeled[remote_address] == table[local_address ^ remote_address]
                cases += 1
    return cases


def verify_bipartite_branches():
    cases = 0
    for a, b, z0, z1, w0, w1 in product((0, 1), repeat=6):
        z, w = (z0, z1), (w0, w1)
        relabeled_z, relabeled_w = xor_relabel(z, a), xor_relabel(w, b)
        (q1, r1), (q2, r2) = lookup_terms(relabeled_z, b) + lookup_terms(relabeled_w, a)
        local_phase = sign(relabeled_z[0] ^ relabeled_w[0])
        ideal_phase = sign(z[a ^ b] ^ w[a ^ b])

        for m1, s1, m2, s2 in product((0, 1), repeat=4):
            numerator = local_phase
            numerator *= corrected_cz_numerator(q1, r1, m1, s1)
            numerator *= corrected_cz_numerator(q2, r2, m2, s2)
            assert numerator == ideal_phase * sign(m1 * s1 + m2 * s2)
            cases += 1
    return cases


if __name__ == "__main__":
    verify_remote_cz()
    print("Remote CZ: all 16 flag and measurement assignments passed.")
    for k in (1, 2, 3):
        count = verify_relabeling(k)
        print(f"k={k}: {count} reversible lookup and relabeling cases passed.")
    count = verify_bipartite_branches()
    print(f"k=1 bipartite circuit: {count} corrected branches passed.")
