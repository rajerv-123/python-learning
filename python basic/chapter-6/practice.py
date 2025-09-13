m1 = int(input("enter the 1st marks"));


m2 = int(input("enter the 2nd marks"));


m3 = int(input("enter the 3rd marks"));


totalPercentage = (100*(m1+m2+m3)) /100;
print(totalPercentage)

if(totalPercentage<50 and totalPercentage <45 and totalPercentage <60):
    print("your are second division");
elif(totalPercentage>60):
    print("your are first divison")
