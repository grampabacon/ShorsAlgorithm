import math
import classical.FastPower as FP


def power(N):
    def is_power(l, r, s, N):
        if l > r:
            return -1
        mid = (l + r) / 2
        ans = FP.fast_power_boolean(mid, s, N)
        if ans == N:
            return mid
        elif ans < N:
            return is_power(mid + 1, r, s, N)
        else:
            return is_power(l, mid - 1, s, N)

    s = int(math.floor(math.log(N, 2))) + 1
    r = int(math.floor(math.sqrt(N))) + 1
    for i in range(2, s):
        ans = is_power(2, r, i, N)
        if ans != -1:
            return ans
    return -1
