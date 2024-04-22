#dictionary is a muttable and stored like this key:value
#The data is stored as key-value pairs a python dictionary
employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
print(type(employee))
print("printing employee data,...")
print(employee)
print()


#creating an empty dictionary
Dict={}
print("Employee Dictionary:")
print(Dict)
print()

#creting a dictionary
#with dict method
Dict=dict({1:"mango",2:"banana"})
print("\n Create dictionary by using dict():")
print(Dict)
print()


#creting a dictionary
#with each item as a pair
Dict=dict([(4,'malli'),(2,'shetty')])
print("\nDictionary with each item as pair")
print(Dict)
print(type(Dict))
print()


employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
print(type(employee))
print("printing data")
print(employee)
print("Name:%s" %employee["name"])
print("age:%d" %employee["age"])
print("salary:%d" %employee["salary"])
print("dob:%s" %employee["dob"])
print()


#adding elements to dictionary one at a time
Dict[0]='Kannan'
Dict[1]='malli'
Dict[2]='hari'
print(Dict)
print()

#with a single key
#The Emp_ages doesn't to exist dict
Dict['Emp_ages'] = 20,30,40  #with parenthesisi or without paranthesis it will execute
print("\n After adding 3 elements...")
print(Dict)
print()


employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
print(type(employee))
print("printing data")
print(employee)
print("printing the details of ne employee")
employee["name"]=input("name:");
employee["age"]=int(input("age:"));
employee["salary"]=int(input("salary:"));
employee["company"]=input("company:");
employee["x-lover"]=input("x-lover -yes or no:");
print("printing new data...")
print(employee)
print()


employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
print(type(employee))
print("printing data")
print(employee)
print("deleting some info of employee data")
del employee["name"]
del employee["company"]
print("printing the modifies employee data")
print(employee)
print("deleting the dictionary: Employee")
del employee
#print("Let try to print again")
#print(employee)
print()


#create a dictionary
Dict1={1:'EZTS', 2:'In-plant training', 3:'college'}
#deleting a key
#using pop() method
pop_key=Dict1.pop(2)
print(Dict1)
print()

#for loop to print all the keys of a  dictionary
employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
for x in employee:
    print(x)
print()

#for loop to print all the values of a  dictionary
employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
for x in employee:
    print(employee[x])
print()


#for loop used to print the items of the dictionary using items()  method
employee={"name":"balaji","age":70,"salary":200000,"company":"EZTS","dob":"2000-15-15"}
for x in employee.items():
    print(employee)
print("-----------")
dict={1: "chinnu", 2: "malli", 3: "hari"}
print(len(dict))
print("-----------")

dict={4: "rcb", 5: "soda", 6: "NA"}
print(sorted(dict))
print("-----------")

dict={1: "chinnu", 2: "malli", 3: "hari"}
#copeing the dict
dict_demo = dict.copy()
print(dict_demo)


dict={1: "chinnu", 2: "malli", 3: "hari"}
#copeing the dict
dict_demo = dict.copy()
#deleting the element
x = dict_demo.pop(1)
print(x)
print(dict_demo)


dict={1: "chinnu", 2: "malli", 3: "hari"}
print(dict_demo.items())


dict={1: "chinnu", 2: "malli", 3: "hari"}
print(dict_demo.get(3))


dict={1: "chinnu", 2: "malli", 3: "hari"}
print(dict_demo.values())


dict={1: "chinnu", 2: "malli", 3: "hari"}
#update method
dict.update({3: "tcs"})
print(dict)

