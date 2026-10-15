#happy number
def is_happy(n):
    seen = set()
    while n!=1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
num = int (input("Enter a number:"))
if is_happy(num):
    print(num,"is a happy number")
else:
    print(num,"is not a happy number")

#duck number
def is_duck(n):
 s = str(n)
 return s[0] !='0' in s[1:] 
num = int(input("Enter a number:"))
if is_duck(num):
  print("duck number")
else:
  print("not a duck number")    
#peterson number or strong number
from math import factorial 
def is_peterson(n):
   return n == sum(factorial(int(d))for d in str(n))
num=int(input("Enter a number"))
if is_peterson(num):
   print("peterson number")
else:
   print("not a peterson number") 