#Operator in Python
# 5+2-8+9*7\2
#5,3,6,7,8,4 ==>Operands
#+,-,*,\,%,==>Operators

#1. Mathematical Operators || Arithmatic Operators :
#   +,-,*,\,%,**,\\

# Addition(+)
# In Integer
num1 = 10
num2 = 20
num3 = num1 + num2
print(f"num1 + num2 = {num3}")
 
# In String
# You can add multiple string
s1 = "Aryan_"
s2 = "Sapsod"
result = s1+s2
print(f"Result = {result},Type of result = {type(result)}")
# O/P = Result = Aryan_Sapsod,Type of result = <class 'str'>

# It is Called Concatination

# Float
f1 = 10.88
f2 = 10.68

result = f1+f2
print(f"Result ={result},Type of result ={type(result)}")
# O/P =Result =21.560000000000002,Type of result =<class 'float'>

# Substraction 
f1 = 10.56
f2 = 21.7
 
result = f1-f2
print(f"Result ={result},Type of result ={type(result)}")

# Multiplication

n1=10
n2=30

Result =n1*n2
print(f"Result ={Result},Type of result = {type(Result)}")
#O/P =Result =300,Type of result = <class 'int'>

# String + Int

s1 = "Aryan"
n1 = 2

result = s1 * n1
print(f"Result ={result}")

# O/P => Result =AryanAryan
l1 = [10,20,30,40,50]
t1 = (10,20,30,40,50)
print(l1)
print("_"*80)
print(t1)

#O/P ==>
# [10, 20, 30, 40, 50]
# ___________________________________________
# (10, 20, 30, 40, 50)
