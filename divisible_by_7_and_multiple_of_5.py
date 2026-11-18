start=int(input("Enter Starting number:"))
end=int(input("Enter ending number:"))
num=start
while num<=end:
    if num % 7==0 and num % 5==0:
        print(num)

    num+=1