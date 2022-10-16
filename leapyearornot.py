print("Enter the Year: ", end="")
y = int(input())

if y%4==0 and y%100!=0:
    print("\n" +str(y)+ " is a Leap Year")
elif y%400==0:
    print("\n" +str(y)+ " is a Leap Year")
else:
    print("\n" +str(y)+ " is not a Leap Year")
