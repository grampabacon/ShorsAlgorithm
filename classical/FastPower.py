# Calculates a^b (mod N)
def fast_power(a, b, N):
    answer = 1
    while b > 0:
        if b % 2:
            answer = answer * a % N
        b = b // 2
        a = a * a
    return answer


def fast_power_boolean(a, b, N):
    answer = 1
    while b > 0:
        if b % 2:
            answer = answer * a
        b = b // 2
        a = a * a
        if answer > N:
            return answer
    return answer
