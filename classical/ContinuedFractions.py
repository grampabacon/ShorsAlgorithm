from GreatestCommonDivisor import extended_gcd


def continued_fractions(y, Q, N):
    fractions = extended_gcd(y, Q)
    depth = 2

    def partial(fractions, depth):
        c = 0
        r = 1

        for i in reversed(range(depth)):
            _c = fractions[i] * r + c
            c, r = r, _c
        return c

    r_cf = 0
    for d in range(depth, len(fractions) + 1):
        _r = partial(fractions, d)
        if _r == r_cf or _r >= N:
            return r_cf
        r_cf = _r

    return r_cf
