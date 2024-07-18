num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

while num2!=0:

    temp=num2
    num2=num1%num2
    num1=temp

print("the GCD of the two numbers is {}".format(num1))
