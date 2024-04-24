# X pattern   
def print_x_pattern(text):
    length = len(text)
    for i in range(length):
        for j in range(length):
            if i == j or j == length - i - 1:
                print(text[j], end="")
            else:
                print(" ", end="")
        print()

name = "Mallikarjun"
print_x_pattern(name)
print()

#Z pattern
def print_z_pattern(text):
    length = len(text)
    for i in range(length):
        if i == 0 or i == length - 1:
            print(text)
        else:
            print(" " * (length - i - 1) + text[i])

name = "Mallikarjun"
print_z_pattern(name)
print()


#V pattern
def print_v_pattern(text):
    length = len(text)
    for i in range(length):
        print(" " * i + text[i] + " " * (2 * (length - i - 1)) + (text[i] if i != length - 1 else ""), end="")
        print()

name = "Mallikarjun"
print_v_pattern(name)
print()

