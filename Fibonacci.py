n=int(input("Enter how many terms:"))
a=0
b=1
for i in range(n):
    print(a,end="")
    new=a+b
    a=b
    b=new