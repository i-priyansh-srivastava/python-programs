'''
# *
# **
# ***
n=int(input("enter no. of rows"))
for i in range(n):
    print("*"*(i+1))
'''


'''
#     *
#    **
#   ***
n=int(input("enter no. of rows"))
for i in range(n):
    print(" "*(n-i-1),"*"*(i+1),sep="")
'''


'''
# ***
# **
# *
n=int(input("enter no. of rows"))
for i in range(n):
    print("*"*(n-i)," "*(i))
'''


'''
# ***
#  **
#   *
n=int(input("enter no. of rows"))
for i in range(n):
    print(" "*(i),"*"*(n-i),sep="")
'''


'''
# AAA
# BBB
# CCC
n=int(input("enter no. of rows"))
for i in range(n):
    print(chr(65+i)*n)
'''


'''
#    A
#   BB
#  CCC
n=int(input("enter no. of rows"))
for i in range(n):
    print(" "*(n-1-i),chr(65+i)*(i+1))
'''


'''
# A
# BB
# CCC
n=int(input("enter the rows"))
for i in range(n):
    print(chr(65+i)*(i+1))
'''

'''
# A
# AB
# ABC
n=int(input("enter the no. of rows"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()
'''


'''
#    *
#   **
#  ***
#   **
#    *
n=int(input("enter the no. of stars in centre of pyramid"))

for i in range(n):
    print(" "*(n-1-i),"*"*(i+1),sep="")

for k in range(n):
    print(" "*(k+1),"*"*(n-1-k),sep="")
'''


'''
# *
# **
# ***
# **
# *
n=int(input("enter the rows"))
p=n//2
for i in range(p+1):
    print("*"*(i+1))

for k in range(p+1):
    print("*"*(p-k))
'''


'''
#    *
#   ***
#  *****
#   ***
#    *

n=int(input("enter number of rows"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    for l in range(i):
        print("*",end="")
    print()
for i in range(n):
    for k in range(i+1):
        print(" ",end="")
    for j in range(n-i-1):
        print("*",end="")
    for k in range(n-i-2):
        print("*",end="")
    
    print() 
'''


'''
# *
# **
# * *
# *  * 
# *****
n=int(input("enter the no. of rows "))
for i in range(n):
    if i==0 or i==n-1:
        print("*"*(i+1))
    else:
        print("*"," "*(i-1),"*",sep="")
'''


'''
# *      * 
# **    **
# ***  ***
# ********


# n=int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(n-i-1):
#         print(" "*2,end="")
#     for l in range(i+1):
#         print("*",end="")
    
#     print()
'''


'''
#name triangle

# P
# RI
# YAN
# SHPR
# IYANS
# s=input("enter strirng to be printed")
# n=int(input("enter rows"))
# x=0
# l=len(s)
# for i in range(n):
#     for j in range(i+1):
#         print(s[x%l],end="")
#         x+=1
#     print()
'''
