num=0
num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
num3=int(input("Enter the number3: "))

if(num2<num1):
    print("max: ", num1)
elif(num2<num3):
    print("max: ", num3)
else:
    print("max: ", num2)