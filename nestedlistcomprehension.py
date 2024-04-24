#nested list comprehesion
matrix=[[j for j in range(5)] for i in range(3)]
print(matrix)

integer_input=list(map(int, input("Enter integer separated by space:").split()))
float_input=list(map(float, input("Enter integer separated by space:").split()))
string_input=list(map(int, input("Enter integer separated by space:").split()))
print("Integer input:",integer_input)
print("float input:",float_input)
print("string input:",string_input)


data=list(map(int, input("Enter integers separated by space:").split()))
data=list(map(int, input("Enter integers separated by space:").split()))
data=extend(input("Enter integers separated by space:").split())