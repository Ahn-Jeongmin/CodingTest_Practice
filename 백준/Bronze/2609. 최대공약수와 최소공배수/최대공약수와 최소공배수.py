def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

gcd_value = gcd(a, b)
lcm_value = (a * b) // gcd_value

print(gcd_value)
print(lcm_value)
