# a = [1,2,3,"Rajeev","shiva","Ponny"];
# i = 0;
# while(i<len(a)):
#     print(a[i]);
#     i+=1;


# n = int(input("enter the number : "))
# i = 1
# while(i < 11):
#     print(f"{n} * {i} = {n*i}");
#     i +=1

n = int(input("enter the number : "));
for i in range(1,n+1):
   print(" " * (n-1), end="")
   print("*" * (2*i-1), end="")
   print("")