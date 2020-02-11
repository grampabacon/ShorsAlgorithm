def modular_exponentiation(a, exp, mod):
    out = 1
    while exp > 0:
        if (exp & 1) == 1:
            out = out * a % mod
        a = (a * a) % mod
        exp = exp >> 1

    return out
