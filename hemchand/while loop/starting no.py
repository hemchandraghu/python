n=int(input("enter the number"))
a=int(input("first digit to check"))
while n!=0:
       d=n%10
       n=n//10
if d==a:
    print("start with a",a)
else:
    print("not start with",a)
