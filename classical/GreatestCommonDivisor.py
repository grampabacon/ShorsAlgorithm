# Find greatest common divisor
def greatest_common_divisor(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a = a % b
        a, b = b, a
    return a
