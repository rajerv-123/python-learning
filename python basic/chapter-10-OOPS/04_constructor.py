class Employee:
    name = "Rajeev"
    language = "Python"
    salary = 1000
    
    def __init__(self):  # dunder __init__ is the constructor method
         # Constructor method (Automatically called when an instance is created)
        # This method is called when an instance of the class is created
        # You can initialize instance attributes here
        print("Employee created")

    def getInfo(info):
        print(f"the salary is {info.salary} and the language is {info.language}")
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I code in {self.language}.")
    
    @staticmethod
    def say_hello():
        print("hello ji how are you?")

rajeev = Employee()
# print(rajeev.salary, rajeev.language)
print(rajeev.name)