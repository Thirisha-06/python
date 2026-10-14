count=0
for n in range(1,51):
 if n % 5==0:
    count+=1
 print("Count:",count)

 #sum off odd number
 total=0
 for n in range(1,20):
   if n % 2!=0:
    total+=n
   print("Sum:",total)

 #div by 3 not by 2
 for n in range(1,31):
   if n % 3 == 0 and n % 2!= 0:
    print(n)

 #count positive or negative
 num =[5,-3,8,-1,0,7,-9,2] 
 positive=0
 negative=0
for n in num:
  if n>0:
   positive+=1
  elif n<0:
   negative+=1
print("Positive:",positive)
print("Negative:",negative)

#largest num without using max
num = [5,-3,8,-1,0,7,-9,2]
Largest = num[0]       
for n in num:
  if n>Largest:
    largest = n
    print("Largest:",largest)
#factorial
num=5
fact=1
for i  in range(1,num+1):
 fact=fact*i
 print("factorial:",fact)
#prime or not
n=7
is_prime=True
for i in range(2,num):
  if num % i == 0:
    is_prime=False
    break
  if is_prime:
    print("Prime number")
  else:
    print("not a prime number")
 
  #sum of digit
  num=1234
  total=0
  while num>0:
    digit=num%10
    total=total+digit
    num=num//10
    print("Sum of digits:",total)
  #nunmber use square is even
  for n in range(1,21):
    square=n*n
    if square%2==0:
      print(n,"->",square)
#armstrong number
n=int(input("Enter a number"))
temp=n
total=0
while temp>0:
  digit=temp%10
  total+=digit**len(str(n))
  temp//=10
  if total==n:
    print("Armstrong number")
  else:
    print("Not Armstrong number") 