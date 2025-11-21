# Union

from ast import arg


set1 ={10,20,30,40,50,60}
set2 ={30,40,50,60,70,}
print(f"s1.union(s2)= {set1.union(set2)}")
print(f"s2.union(s1= {set2.union(set1)})")

# Intersection

print(f" s1.intersection(s2) = {set1.intersection(set2)}")
print(f"s2.intersection(s1)= {set2.intersection(set1)}")

# Differences

print(f"s1-s2= {set1-set2}")
print(f"s2-s1= {set2-set1}")

def fun():
    s1={10,20,30,40,50,60}
    s1.add(60)
    print(f"values of s1= {s1}")
fun()

def fun1():
    s1={10,20,30,40,50,60}
    s1.discard(60)
    print(f"values of s1= {s1}")
fun1()

def fun2():
    s1={10,20,30,40,50}
    s1.remove(20)
    print(f"values of s1 = {s1}")
fun2()

