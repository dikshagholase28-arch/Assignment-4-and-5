n = int(input("Enter n: "))
i = 1
term = 1
total = 0

while i <= n:
    total = total + term
    term = term * 2
    i += 1

print("Sum =", total)