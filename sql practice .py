import sqlite3
# conn=sqlite3.connect("sql practice.db")
# conn.execute('''
#     create table employee(
#         emp_id INT AUTO_INCREMENT PRIMARY KEY,
#         emp_name VARCHAR(50),
#         emp_address VARCHAR(10),
#         emp_email VARCHAR(30)
#     )
#       ''')
# conn.close()   

#Insert Query
# conn=sqlite3.connect("sql practice.db")
# ins='''
#     insert into employee(emp_name,emp_address,emp_email)
#     VALUES('NITESH','BANGLORE',"nitesh@gmail.com")
#     '''
# conn.execute(ins)
# conn.commit()
# conn.close() 

#Select Query
# conn=sqlite3.connect("sql practice.db")
# data=conn.execute("SELECT*FROM employee")
# print("employee id","employee name","employee address","employee email")
# for n in data:
#     #print(n)
#     print(n[0],"    ",n[1],"    ",n[2],"    ",n[3])

#if we want to see few data we use limit key word 
conn=sqlite3.connect("sql practice.db")
data=conn.execute("SELECT * FROM employee limit 0,5")
print("Employee_id","    ","Employee_name","    ","Employee_address","    ","Employee_email")
for n in data:
    print(n[0],"   ",n[1],"   ",n[2],"   ",n[3])     

#Delete Query
conn=sqlite3.connect("sql practice.db")
emp_id= input("Enter the Employee_id :- ")
conn.execute("DELETE FROM employee where emp_id="+emp_id)
conn.commit()
conn.close()