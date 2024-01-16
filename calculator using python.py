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
