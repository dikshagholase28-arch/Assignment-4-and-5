num=int(input("Enter a Number:"))
i=1
total=0
while i < num:
    if num % i ==0:
        total +=i
    i +=1

if total == num:
    print("perfect Number")
else:
    print("Not a Perfect Number")