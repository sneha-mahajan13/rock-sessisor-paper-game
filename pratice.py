#program to peint hello world
print("hello world")

#program to print addition of two numbers
a=2
b=6
print("sum",a+b)

#program to print"hello world I'm coder
print("Hello world i'm coder")

#Variables in python
a=100
b=4000
print(a,b)

#program
name="sneha"
age=20

#program of strings
name="Sneha Mahajan"

print(name.upper())
print(name.lower())
print(name.find('e'))
print(name.replace("sneha","purvi"))
print('S'in name)

#program to concnate string
a="hello"
b="moon"
print(a+" "+b)

#programs using operators
#ASSIGMENT OPERATORS
x=5
print(x)
x+=5
print(x)
x-=5
print(x)
x*=5
print(x)


#cOMPRESION OPERATORS IN PYTHON
S=100
s=50
print(S==s)
print(S!=s)
print(S>s)
print(S<s)
print(S>=s)
print(S<=s)

#dictionary program
d={
    'name' : 'python',
    'fee' : 8000,
    'deuration':'2 m0nths'
}
for a in d:
    print(d[a])

 
#program for taking input
a=int(input("enter the value :"))
b=int(input("enter the value:"))
print(a+b)

#dictionary program
course={
    'php':{'duration':'2 month','fee':4000},
    'pyhton':{'duration':'4 month','fee':7000},
    'java':{'duration':'6 month','fee':12000}
}
print(course)
course['java']['fee']=9000

for k,v in course.items():
    print(k,v['duration'],v['fee'])

#Logical operators
x=1023
y=5000
print(x==1032 and x<y)
print(x==1032 and x<y and x==y)
print(x==1032 or x>y)
print(x==1032 or y>x or x==y)
print(x!=1032)
print(y==5000)

#Membership operators
string1 = "Hellow world"
print('h' in string1)

String2 = "Sneha Mahajan"
print('k'in String2)

list = [10,20,33,45,67,88]
print(33 in list)
print(45 not in list)


#Identity Operators
x=100
y=100
print(x is y)
print(x is not y)

#Bitwise Operators
x=10
y=8
print(bin(x))
print(bin(y))
print(x&y)
print(bin(x&y))
print(x|y)
print(bin(x| y))
print(x^y)
print(bin(x^y))

#Data Types in python
#Number data type
a=10
print(a, "is of tyye",type(a) )              #integer
b=2.8
print(b, "is of type",type(b))               #float
c=1+2j
print(c, "is of type",type(c))               #complex

#String data type
#Double quotes
s="this is a string"
print(s,type(s))
#single quotes
s='Hello world @1234'
print(s,type(s))
#triple quotes
s='''Hello world 
i am 
sneha mahajan'''
print(s,type(s))

#liat in python
l = [10,200,4.56,"Ss"]
print(l,type(l))

#chnaging value in list
a=[12,'Hello',4.64]
a[2]="shrutii"
print(a,type(a))

#Tuple in python
t=(100,'sneha',6.78,"shrutii")
print(t,type(t))
s=(123,"hello world",765)

#random number 
import random
cnumber=random.randrange(1,101)
userInput=int(input("enter number --"))
if userInput>cnumber:
    print("Computer number :",cnumber)
    print("your guess number is high ")
elif cnumber<userInput:
    print("computer number :",cnumber)
    print("your guess number is low ")
else:
    print("computer number :",cnumber)
    print("your guess number is equal")    

#pickle dump()
import pickle 
l=[10,20,30,40,50]
file=open("Ss","wb")
pickle.dump(l,file)
file.close()

#Pickle load()
import pickle
file=open("Ss","rb")
l=pickle.load(file)
print(l)


#Rock paper scissor game 
import random
l=["rock","scissor","paper"]
'''
rock vs paper --> paper wins
rock vs scissor --> rock wins
scissor vs paper --> scissor wins 
'''

while True:
    Ccount=0
    Ucount=0
    UC=int(input('''
Game start.....
1 yes|play
2 no|exit
    '''))
    if UC==1:
        for a in range(1,6):
            userInput=int(input('''
1 rock
2 scissor
3 paper
            '''))
            if userInput==1:
                Uchoice="rock"
            elif userInput==2:
                Uchoice="scissor"
            elif userInput==3:
                Uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==Uchoice:
                   print("Computer Value :",Cchoice)
                   print("User value :",Uchoice)
                   print("Game Draw")
                   Ucount=Ucount+1
                   Ccount=Ccount+1
            elif (Uchoice=="rock" and Cchoice=="scissor")or(Uchoice=="paper" and Cchoice=="rock")or(Uchoice=="scissor" and Cchoice=="paper"):
                    print("Useer value :",Uchoice)
                    print("Computer value :",Cchoice)
                    print("You win")
                    Ucount=Ucount+1
            else :
                    print("Useer value :",Uchoice)
                    print("Computer value :",Cchoice)
                    print("Computer win")
                    Ccount=Ccount+1
        if Ucount==Ccount:
                    print("Final Game Drow")
                    print("USER SCORE :",Ucount)
                    print("Computer Score :",Ccount)
        elif Ucount>Ccount:
                    print("Final you win")
                    print("USER SCORE :",Ucount)
                    print("Computer Score :",Ccount)
        else: 
                    print("Computer win the game..")                                                                  
                    print("USER SCORE :",Ucount)
                    print("Computer Score :",Ccount)
    else:
        break;           


#JSON program
import json 
d={
    'course_name':'python',
    'fee':15000
}
f=json.dumps(d)
print(type(f))
print(f)

#Converting JSON to python object
import json
x='{"name":"sneha","subject":"CS","year":"3rd"}'
k=json.loads(x)
print(type(k))
print(k)
for p in k:
    print(p)
    print(p,k[p])

#Oop's in python (Class,Object)
class DemoClass:
    a=10
demo_object=DemoClass()            #1 object 1 class
print(demo_object.a)    


class DemoClass:
    a=10
demo_object1=DemoClass()          #2 objects 1 class
demo_object2=DemoClass()
print(demo_object1.a)
print(demo_object2.a)    
 
#Methods inside the class 
class MethodClass:
    a=10
    def sumvalue(self):
        print(10+15)
        print(58*59)
demo_object=MethodClass()
print(demo_object.a)
demo_object.sumvalue()

#MEthods and Constructors
class PracticeClass:
    a=10
    def showvalue(self):
        print(self.a)

obj=PracticeClass()
obj.showvalue()

class MethodArguments:
    a=100
    def showvalue(self):
        print(self.a)
    def print_value(self,a,b):
        print(a+b)
        print(a*b)
object=MethodArguments()
object.showvalue()
object.print_value(134,1)

#Method Variables
class Variables:
    a=4
    def showvalue(self):
        self.c=self.a*self.a
        self.k=self.a+self.a
        print(self.c)
        print(self.k)
print_output=Variables()
print_output.showvalue()        

#Constructors
class SnehaMahajan:
    def __init__(self):
        print("hello world !")
obj=SnehaMahajan()

#Inheritance
#1.Single Inheritance
class A:
    def displayA(self):
        print("Hello World A")
class B(A):
    def displayB(self):
        print("HEllo World B")
obj=B()
obj.displayA()
obj.displayB()                

#2.Multilevel Inheritance
class A:
    def displayA(self):
        print("Hello A")
class B(A):
    def displayB(self):
        print("Hii B")
class C(B):
    def displayC(self):
        print("Bonjour C")      

obj=C()
obj.displayA()
obj.displayB() 
obj.displayC()  

#3.Multiple Inheritance
class A:
    def displayA(self):
        print("Shritii A")
class B:
    def displayB(self):
        print("Sneha B")
class C(A,B):
    def displayC(self):
        print("Purvii C")      

obj=C()
obj.displayA()
obj.displayB() 
obj.displayC()  

#Encapsulation (Getter and Setter)
class Ss:
    def __init__(self):
        self.__name=" "
    def getname(self):
        return self.__name
    def setname(self,S):
        self.__name=S
obj=Ss()
obj.setname("Purvii")
n=obj.getname()
print(n)  

#Encapsulation
class Student:
    __name="Ravi"             #private variable
    def __displayinfo(self):
        print("hii my name is sneha")
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
obj=Student ()    


#PolyMorphism
#length of list and string
l=[10,20,44,69,86]
print(len(l))
s="welcome"
print(len(s))

#OverLoading Function
class Ss:
    def displayoutput(self,name=' '):
        print("hii my name is " +name)

obj=Ss()
obj.displayoutput()                      #hii my name is
obj.displayoutput('preeti')              #hii my name is preeti

#Overriding Function
class Ss:
    def displayvalue(self):
        print('hello miss Gupta')
class Sneha:
    def displayvalue(self):
        print('hello miss mahajan')
                                
obj=Sneha()
obj.displayvalue()                    #function of class sneha will override the function of of class Ss

#calling of parent function using super ()
class Shruti:
    def print_value(self):
        print("hello miss gupta")
class Sneha(Shruti):
    def print_value(self):
        super().print_value()
        print("hello miss mahajan")        
obj=Sneha()
obj.print_value()

#method overloading 
class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of rectangle :",(a*b))
        elif a!=None:
            print("Area of square :",(a*a))
        else :
            print("nothing to find")
obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)

#Project Bike Rental System
class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("total Bikes :",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-1
            print("Total Price :",q*100)
            print("Total Bike :",self.stock)
while True:
    obj=BikeShop(100)
    uc=int(input('''
    1. Display Bike Stock
    2. rent a Bike
    3.exit
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the Qty :"))
        obj.rentForBike(n)
    else:
        break                           

#SyntaxError
#a=10
#b=20
#if a==b
#    print("no")
#else
#    print("yes")    
        
#LOgical Error
#print(a/0)        #ZeroDivisionError

#l=[1,2,3,4]
#print(l[8])      #IndexError

print("Syntax Error program is executed")

#sqlite in python for DB browser
#import sqlite3
#conn=sqlite3.connect("sqlite.db")
#conn.execute('''
 #      create table Student(
  #     st_id INT AUTO_INCEMENT PRIMARY KEY,
  #     st_name VARCHAR(50),
   #   st_email VARCHAR(30)
    #   )
    #  ''')
#conn.close()  

#insert Query 
# import sqlite3
# conn=sqlite3.connect("sqlite.db")

# ins='''
#       insert into Student(st_name,st_class,st_email)VALUES
#       'Nisha','9th',"nisha@gmail.com")  
#   '''
# conn.execute(ins)
# conn.commit()
# conn.close()  

# #SELECT QUERY
# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# data=conn.execute("SELECT * FROM Student  limit 0,1")
# print("Student Id"   ,"Student Name"   ,"Student Class"   ,"Student Email")
# for n in data:
#     #print(n)                     #Tuple
#     print(n[0],"   ",n[1],"    ",n[2],"    ",n[3])


# #DELETE QUERY
# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# st_id=input("Enter the student Id :- ")
# conn.execute("DELETE FROM Student where st_id="+st_id)
# conn.commit()
# conn.close()

# #Update Query
# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# conn.execute('''
#    update student set st_name="Rupesh",st_class="10th",st_email="rupesh@gmail.com" where st_id=7 
#    ''')
# conn.commit()
# conn.close()

# #Searching Query
# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# #Without filter
# data=conn.execute("SELECT * FROM Student")
# print("Student Id" , "Student Name" , "Student Class" , "Student Email" )
# for n in data:
#     print(n[0], "  " , n[1], "  " , n[2], "  " ,n[3])

# print(" ")
# print(" ")

# #with filter
# data=conn.execute("SELECT * FROM Student where st_name='Sneha'")
# for n in data:
#     print(n[0], "  " , n[1], "  " , n[2], "  " ,n[3])

# print(" ")
# print(" ")    

# #Searching Query by taking input form user 
# st_name=input("Enter the Name :- ")
# data=conn.execute("SELECT * FROM Student where st_name='"+st_name+"'")
# for n in data:
#     print(n[0], "  " , n[1], "  " , n[2], "  " ,n[3])

# print(" ")
# print(" ")    

# #Searching of data by one letter
# st_name=input("Enter the letter of student name :- ")
# data=conn.execute("SELECT * FROM Student where st_name like '%"+st_name+"%'")
# for n in data:
#     print(n[0], "  " , n[1], "  " , n[2], "  " ,n[3])

# print(" ")
# print(" ")        

# #Checking data using more than on condition
# #and : both the condition have to be true

# st_name=input("Enter the letter of student name :- ")
# st_class=input("Enter the class of student :- ")
# data=conn.execute("SELECT * FROM Student where st_name like '%"+st_name+"%' and st_class='"+st_class+"'")
# for n in data:
#     print(n[0], "  " , n[1], "  " , n[2], "  " ,n[3])

# #or : atleast one condition have to be true
# st_name=input("Enter the letter of student name :- ")
# st_class=input("Enter the class of student :- ")
# data=conn.execute("SELECT * FROM Student where st_name like '%"+st_name+"%' or st_class='"+st_class+"'")
# for n in data:
#     print(n[0], "  " , n[1], "  " , n[2], "  " ,n[3])


 
# #SQlite - join clause
# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# print("Student Id" , "Student Name" , "Student Fee")
# data=conn.execute("SELECT f.st_id,s.st_name,f.fee_amount FROM Fee as f inner join student as s on f.st_id=s.st_id")
# for a in data:
#     print(a)
# conn.close()

x=-7.5
print(abs(x))
 
import math
x=12
print(math.exp(x)) 
print(math.e)
print(math.pi)

#calendar print
import calendar
year=2024
month=1
x=calendar.month(year,month)
print(x)

#print emojis in python program

print("\U0001F600")
print("\U0001F618")
print("\U0001F917")
print("\U0001F62A")
print("\U0001F637")
print("\U0001f600")

#Cristmas tree
import numpy as np 
x=np.arange(7,16)
y=np.arange(1,18,2)
z=np.column_stack((x[::-1],y))
for i,j in z:
    print(''*i+'*'*j)
for r in range(3):
    print(' '*13,' || ')
print(' '*12, end = '\======/')
print('')        
