class Person:
    def __init__(self, name, age,address,team):
        self.name=name
        self.age=age
        self.address=address
        self.team=team
        
class Student(Person):
    def  isStudent(self):
        return f"{self.name} is a Student,\n{self.age} is a age,\n{self.team} is faviourt team,\n{self.address} is city of his"
    
sir=Student("Mallikarjun",20,"Bidar","RCB")
print(sir.isStudent())


