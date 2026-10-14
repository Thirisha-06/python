#number is new number or not
n=int(input("Enter a number"))
square=n*n
total=0
while square>0:
    total+=square%10
    square//10
    if total==n:
        print(n,"is a neon number")
    else:
        print(n,"not a Neon number")
#num is perfect or not
n=int(input("Enter a number"))
total=0
for i in range(1,n):
    if n%i==0:
        total+=i
        if total==n and n>0:
         print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
 #palindrome or not
n=int(input("enter a number"))
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev+10+digit
    temp//=10
    if rev==n:
        print(n,"is a palindrome num")
    else:
        print(n,"is not a palindrome num")  
        
#automorphic or not
n=int(input("Enter a number"))
square=n*n
digits=len(str(n))
last=Square%(10**digits)
if last==n:
    print(n,"is a automorphic")
else:
    print(n,"is not automorphic")           
              