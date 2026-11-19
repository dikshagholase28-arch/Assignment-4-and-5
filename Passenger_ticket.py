n = int(input("Enter number of Passenger:"))
cost = int(input("Enter ticket cost:"))

total = 0

for i in range(1, n+1):
    age = int(input("Enter age:"))

    if age < 12:
        amount = cost - (cost * 30 / 100)

    elif age > 59:
        amount = cost - (cost * 50 / 100)

    else:
        amount = cost

    print("Ticket Amount:", amount)

    total = total + amount

print("Total Amount:", total)
