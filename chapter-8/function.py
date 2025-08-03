#function defination

# def add():
#     a = int(input("enter the no. : "))
#     b = int(input("enter the no. : "))

#     c = a +b;
#     print(c)

# #function call

# add()



# def greetHello():
#     print("Hello !")


# greetHello();


def factorial(num):
    if(num == 0 or num == 1):
        return 1;
    return num * factorial(num-1);



num = int(input("enter the num: "));
print(factorial(num))