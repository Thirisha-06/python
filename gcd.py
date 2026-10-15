#gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("First number: "))
y = int(input("Second number: "))
print("GCD =", gcd(abs(x), abs(y)))