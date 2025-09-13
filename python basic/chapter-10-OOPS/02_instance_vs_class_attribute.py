class Employee:
    name = "Rajeev"    #this is the class attribute
    language = "Python"
    salary = 1200000

rajeev = Employee();
# print(rajeev.salar,y,rajeev.language)
print(rajeev.name)

rajeev.name = "Rajeev Patel"  # here we update the class instance now output will be this rajeev patel 
print(rajeev.name,rajeev.language,rajeev.salary);