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


