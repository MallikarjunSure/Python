numbers=[10,20,30,40,50]
 #List comprehension to create new list
double_number=[num*2 for num in numbers]
print(double_number)
print()


numbers=[10,20,30,40,50]
square_numbers=[]
#for loop to square elements
for num in numbers:
    square_numbers.append(num*num)
print(square_numbers)
print()


numbers=[10,20,30,40,50]
#createb a new list using list comprehension
square_numbers=[num*num for num in numbers]
print(square_numbers)
print()


#Conditionals in list comprehension
#[expression for item in list if condition == True]
#filtering even numbers from
even_numbers=[num for num in range(1,10) if num%2==0]
print(even_numbers)
print()


word="malli"
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
#Find vowel in the string "malli"
result1=[char for char in word if char in vowels]
print(result1)
#Find consonants in the string "malli"
result2=[char for char in word if char in consonants]
print(result2)