'''
#ARITHMETIC OPERATIONS
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# s=a+b
# p=a*b
# q=(a//b)
# div=divmod(a,b)
# d=a-b
# print("sum is {} difference is {} product is {} and quotient in integer is {} and quotient and remainer is {}" .format(s,d,p,q,div))
'''


'''
#ARMSTRONG NUMBER
# n=int(input("enter number"))
# k=n
# r=0
# arm=0
# p=len(str(n))
# while(n>0):
#     r=n%10
#     n=n//10
#     arm=arm+(r**p)
    
# if (arm==k):
#     print("armstrong number")
# else:
#     print("not an armstrong number")
'''


'''
#PERFECT NUMBER
# n=int(input("enter number"))
# s=0
# for i in range(1,n,1):
#     if (n%i==0):
#         s=s+i
# if s==n:
#     print("perfect number")
# else:
#     print("not a perfect number")
'''


'''
#PRIME NUMBER OR NOT
num=int(input("enter the number"))
c=0
for i in range(1,num+1,1):
    if num%i==0:
        c=c+1
if c==2:
    print(num,"is prime number")   
else:
    print(num,"is not a prime number") 
'''


'''
# PALLINDROME NUMBER
# n=int(input("emter number"))
# k=n
# p=0
# r=0
# while(n>0):
#     r=n%10
#     n//=10
#     p=p*10+r
# if k==p:
#     print("{} is a pallindrome".format(k))
# else:
#     print("{} is not a pallindromic number".format(k))
''' 

'''
#ARMSTRONG NUMBER BETWEEEN PRE-DEFINED RANGES
for num in range(150,154):
    arm=0
    p=len(str(num))
    k=num
    while(num>0):
        r=num%10
        num=num//10
        arm=arm+r**p
    if arm==k:
        print(k)
'''
