print("Enter the Number: ")
num = int(input())

p = 0
for i in range(2, num):
    if num%i==0:
        p = 1
        break

if p==0:
    print("\nIt is a Prime Number")
else:
    print("\nIt is not a Prime Number")
