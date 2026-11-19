x = int(input("Enter x: "))
n = int(input("Enter n: "))
i = 1
total = 0
sign = 1

while i <= n:
    total = total + sign * (x ** i) / (2 * i - 1)
    sign = sign * -1
    i += 1

print("Sum =", total)