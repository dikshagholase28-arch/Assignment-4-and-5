n=int(input("Enter number of students:"))
sum_per=0
for i in range(1,n+1):
    total = 0 
for j in range(1,6):
    marks = int(input("Enter marks:"))
    total= total + marks
    per = total / 5
    print("percentage:",per)
    sum_per= sum_per + per

    avg = sum_per/n
    print("Average Percentage")
