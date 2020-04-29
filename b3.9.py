"""program make a simple calculato that can add,subtract,multiply and
divide using functons"""
#thí function adds two numbers def add(x,y)
 return x + y
#this dunctions subtract two number def subtract(x,y):
 return x - y
#this function multiplies two number def multiplies(x,y):
 return x * y
#this function divides two number der divide(x,y)
 return x / y
print("select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#take input from the user
choice=input("enter choice(1/2/3/4):")
num1=int(input("enter first nuber:"))
num2=int(input("enter second number:"))
if choice=='1':
    print(num1,"+",num2,"=".add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=".divide(num1,num2))
else:
    print("invalid input")