start=int(input("Enter Starting number:"))
end=int(input("Enter ending number:"))
divisor=int(input("enter divisor:"))
num = start
while num<=end:
    if num % divisor==0:
        print(num)
    num+=1
    