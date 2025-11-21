# for i in range(1,5):
#     for j in range(65,69):
#         print(chr(j),end =' ')
######################################
#     print()

# for i in range(65,69):
#     for j in range(1,5):
#         print(chr(j),end=' ')
#     print()

#     # output==>
#     #     A A A A 
#     #     B B B B
#     #     C C C C
#     #     D D D D

##################################################

#     for i in range(1,26):
#         for j in range(65,96):
#             # print(chr(i),end=' ')/
# ch = 0
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(ch+65)+" ",end=' ')
#         if (ch<26):
#             ch +=1
#         else:
#             ch=0

#     print()
# n =5
# ch=0
# for i in range(97,122):
#     for j in range(1,5):
#         print(chr(i),end=" ")
#         if (i):
#             i +=1

#         else:
#             i=0
# print()


# n = 5
# ch = 0
# for i in range(1,n+1):
#     for j in range(1,6):
#         print(chr(ch+97)+' ',end="")
#         if ch<26:
#             ch = + 1
#         else:
#             ch = 0
#     print()

# ch=0
# for i in range(1,6):
#     for j in range(97,122):
#         print(chr(ch + 97)+" ", end="")
#         if ch<26:
#             ch=+1
#         else:
#             ch=0
#     print()

#############################################

# n = 5
# ch = 0
# for x in range(1,4): 
 
#  for y in range(1,4):
  
#   print(chr(65)+" ",end="")
# if ch<26:
#     ch+=1
# else:
#     ch = 0
# print()

# n = 5
# ch = 0

# for i in range(1,5): #ubha
#     for j in range(1,2):#adwa
#         print(chr(97)+"",end=" ")
#         print(chr(98)+"",end=" ")
#         print(chr(99)+"",end=" ")
#         print(chr(100)+"",end=" ")
#         print(chr(101)+"",end=" ")
#         print(chr(102)+"",end=" ")
#         print(chr(103)+"",end=" ")
#         print(chr(104)+"",end=" ")
#         print(chr(105)+"",end=" ")
#         print(chr(106)+"",end=" ")
#         print(chr(107)+"",end=" ")
#         print(chr(108)+"",end=" ")
#         print(chr(109)+"",end=" ")
#         print(chr(110)+"",end=" ")
#         print(chr(111)+"",end=" ")
#         print(chr(112)+"",end=" ")
        

#         print(chr(122)+"",end=" ")
#         if ch<0:
#             ch=+1
#         else:
#             ch=0
#     print()





############################################


# n = 5
# a = 0
# for i in range(n):
#     for j in range(n):
#          print(chr(97+a),end=" ")
#          a = (a+1) % 26       
#     print()
# a b c d e 
# f g h i j
# k l m n o
# p q r s t
# u v w x y



# for i in range(1,6):
#     for j in range(97,102):
#         print(chr(j),end=" ")
#     print()

#######################################

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *

###################################################


# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,6):
#         print(6-j,end=" ")
#     print()

# 5 4 3 2 1 
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(1,6):
#         print(6-i,end=" ")
#     print()
# 5 5 5 5 5 
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1
# a=1
# for i in range(1,6):
#     for j in range(1,6):
#         print(format(a),end=" ")
#         a+=1
#     print()  

# 1 2 3 4 5 
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25


# a = 1
# for i in range(1,6):
#     for j in range(1,6):
#         print(format(a),end=" ")
#         a +=2
#     print()

# 1 3 5 7 9 
# 11 13 15 17 19
# 21 23 25 27 29
# 31 33 35 37 39
# 41 43 45 47 49

# a=2
# for i in range(1,6):
#     for j in range(1,6):
#         print(format(a),end=" ")
#         a +=2
#     print()

# 2 4 6 8 10 
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# 42 44 46 48 50

a=1
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
        a+=1
    print()
print("\n")
# 1 2 3 4 5 
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25


for i in range(1,6):
    for j in range(1,4):
        print(j,i,end=" ")
        
    print()

print("\n")

# 1 1 2 1 3 1 
# 1 2 2 2 3 2
# 1 3 2 3 3 3
# 1 4 2 4 3 4
# 1 5 2 5 3 5

a=3
for i in range(1,6):
    for j in range(2,4):
        print(a*2,end=" ")
        a+=3
    print()



#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


print("\n")

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("\n")

for i in range(6,j+1):
    for j in range(1,6):
        print("*",end=" ")
    print()