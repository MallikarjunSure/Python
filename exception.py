#try:
   # code that may cause exception
#except:
   # code to run when exception occcurs
   
#balaji=5/0
#prin(balaji)


try:
    num=0
    deno=10
    result=num/deno
    print(result)
except:
    print("Error: Denominator ")
    
   
try:
    even_numbers=[2,4,6,8]
    a=even_numbers[6]
    
except ZeroDivisionError:
    print("Denominator csnnot be 0.")
    
except IndexError:
    print("Index out of bounds.")
    
 #program to print the reciprocal or even number   
try:
    num=int(input("Enter a number:"))
    assert num%2==0
    reciprocal=1/num
    print(reciprocal)
except:
    print("not even number")
else:
    reciprocal=1/num
    print(reciprocal)
   
    
   
