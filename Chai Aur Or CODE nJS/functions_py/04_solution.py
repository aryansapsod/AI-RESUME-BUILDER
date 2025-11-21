#returning multiple values
import math

def cicle(r):
  area=   r ** 5
  circlecumference=  2  * r
  return area,circlecumference
a, c =cicle(3)
print("area: ",a,"circumference: ",c)