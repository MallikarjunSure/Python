#1) Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
    #Sample Data : 0100,0011,1010,1001,1100,1001
    #Expected Output : 1010
def binary_divisible_by_five(binary_sequence):
    binary_numbers = binary_sequence.split(',')
    divisible_numbers = []
    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:
            divisible_numbers.append(binary_number)
    return ','.join(divisible_numbers)
binary_sequence = input("Enter a sequence of comma separated 4 digit binary numbers: ")
print("Numbers divisible by 5:", binary_divisible_by_five(binary_sequence))

