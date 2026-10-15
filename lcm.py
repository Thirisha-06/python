#lcm of 2num
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    a, b = abs(a), abs(b)
    big = max(a, b)
    small = min(a, b)
    m = big
    while m % small != 0:
        m += big
    return m

x = int(input("First number: "))
y = int(input("Second number: "))
print("LCM =", lcm(x, y))