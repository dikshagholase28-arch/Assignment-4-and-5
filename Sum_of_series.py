a = int(input("Enter a: "))
i = 1
total = 0

while i <= 10:
    total = total + (a ** i) / i
    i += 1

print("Sum =", total)