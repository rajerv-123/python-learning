class Employee:
    name = "Rajeev"    #this is the class attribute
    language = "Python"
    salary = 1200000

    def getInfo(info):
        print(f"the salary is {info.salary} and the language is {info.language}");

    def greet(self):  # here self is the instance of the class
        # self is used to access the instance attributes and methods
        # self.name = "Rajeev Patel"  # this will update the instance attribute
        # self.language = "Python"
        print(f"Hello, my name is {self.name} and I code in {self.language}.")
    @staticmethod # static method does not take self or cls as first argument
    def say_hello():
        print("hello ji how are you?");

rajeev = Employee();
# print(rajeev.salary,rajeev.language)
print(rajeev.name)

rajeev.name = "Rajeev Patel"  # here we update the class instance now output will be this rajeev patel 
# print(rajeev.name,rajeev.language,rajeev.salary);
rajeev.greet()