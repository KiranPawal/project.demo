num1=int(input("Enter the first number:"))
sign=input("Choose the operation(+,/,-,*,%):")
num2=int(input("Enter the second number:"))

if sign=='+':
    print("Addition of number is:",num1+num2)
    
if sign=='-':
    print("Substraction of number is:",num1-num2)
    
if sign=='/':
    print("Division number is:",num1/num2)

if sign=='*':
    print("Multiplication of number is:",num1*num2)
    
if sign=='%':
    print("Modulus of number is:",num1%num2)