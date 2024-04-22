num1=int(input("enter the num1="))
num2=int(input("enter the num2="))
if(num1>num2):
    print(num1,'num1 is greater')
elif(num1==num2):
    print(num1,num2,'both are same')
else:
    print(num2,'num2 is greater')



num1=int(input("enter the num1="))
num2=int(input("enter the num2="))
print('num1 is greater' if num1>num2 else 'both are same' if num1==num2 else 'num2 is greater')


a=50
b=60
c=150
print('a' if a>b and a>c else 'b' if b>c else 'c')