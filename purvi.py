#program to print addition of two numbers
a=12
b=8
print("addition : ",a+b)

#program to print hello world 
print("hello world","iam coder")

print("hello world","i'am sneha",88)

print("Hello")
print("'hello'")
print('"hello world"')
print("hello \n Byee")
print("hello")
print()
print("hii")
print("my maaths marks is 100")
print("my maths is",100,"my physics marks is",90)

#Variavbles in python
a=4
b=6
(print(a,b))

name="shruti"
age=20
print(name)
print(age)

#to fond address of variables
a=12
b=20
print(id(a),id(b))

name="sneha"
age=33

name="purvi"
age=12
print(name)
print(age)

#program
name="Tony Stark"
age=51
tony_is_genius=True

print(name)
print(age)
print(tony_is_genius)

#Tyoe Conversion
old_age=22
new_age=int(old_age)+3
print(new_age)

first= 64
second=42
Sum=int(first)+int(second)
print(Sum)

first=2
second=4
sum=first+second
print(sum)

#Strings in python
mame="Sneha Mahajan"
print(name.upper())

name="shruti gupta"
print(name.lower())

#to fond letter form string
#name="sneha shruti"
#print(name.find(s))
#print(name.find(a))
#print(name.find(d))

#replace string in python
name="sneha mahajan"
print(name.replace("sneha","purvi"))

name="purvi"
print(name.replace("p","s"))  

#er or word in string 
name="shruti gupta"
print('s'in name)
print('k'in name)

name="Sneha shruti"
print("shruti"in name)
print("neha"in name)

#Concatenation of string in python
a='hello'
b="sneha"
print(a+" "+b)

a=12
b=6
print(a+b)

#program for taking input form the user 
#integer                                                                                                                                                              
a=int(input("enter the value :"))
b=int(input("enter the value:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#Float
a=float(input("enter the value :"))
b=float(input("enter the value:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#eval
a=eval(input("enter the value :"))
b=eval(input("enter the value:")) 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Conditional Statements
#If statement
a=int(input("enter a:"))
if a%2==0:
    print("even number")

#If else statement
a=int(input("enter a: "))
if a%2==0:
    print("even number")
else:
    print("odd number")    

#elif else Statement
per=int(input("enter percentage :"))
if per>80:
    print("first division")
elif per>=60:
    print("second division")
elif per>=45:
    print("third division")
else:
    print("fail in exam")

#cALCULATOR USING CONDITIONAL STATEMENT IN PYTHON
first=int(input("number1:"))
operator=input("enter(+,-,*,/,%):")
second=int(input("enter number2:"))
if operator=='+':
    print(first+second)
elif operator=='-':
    print(first-second)
elif operator=='*':
    print(first*second)
elif operator=='/':
    print(first/second)
elif operator=='%':
    print(first%second)
else:
    print("invalid operation")

#Loops in puthon
#for loop
for n in range(10):
    print(n)
for p in range(4):
    print("hello world") 
for n in range(1,9):
    print(n)
for k in range(1,10,2):
    print(k)
for a in range(1,11):
    print("2*",a,"=",2*a)

i=int(input("enter i:"))
for p in range(1,11):
    print(i,"*",n,"=",i*n)
for w in range(1,5):
    print("I'M SORRY")

#reverse table by taking input form user 
a=int(input("enter a : "))
for n in range(10,0,-1):
    print(a,"*",n,"=",a*n)

#print sneha 10 times using reverse loop with counting
for n in range(10,0,-1):
    print(n,"SNEHA MAHAJAN")

#while loop
i=1
while i<=10:
    print(i)
    i=i+1      

j=1
while j<=15:
    print(j,"hello world")
    j=j+1

#reverse counting using whie loop
i=10
while i>=1:
    print(i,"hello moon")
    i=i-1

#STRINGS IN PYTHON
a="SNeha Mahajan"
print(type(a))
print(a[4])        #left to right indexing
print(a[8])        
print(a[-2])       #right to left indexing

#String slicing
#left to right slicing
a="hello i am a coder"
print(a[0: 6])
print(a[0:  :2])
print(a[0:18])

#right to left slicing
a="najaham ahens"
print(a[0:13])
print(a[0: :2])

s="hello world"
print(s[-1: :-1])
print(s[0:11])

#String iteration in python
a="hello i am a coder"
t=len(a)
print(t)
for k in range(t):
    print(a[k])

#REverse string iteration
a="hello moon i'm earth"
t=len(a)
for p in range(t-1,-1,-1):
    print(a[p])

 
















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         








 