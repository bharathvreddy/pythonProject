# # def gcd(n,m):
# #     if m==0:
# #         return n
# #     else:
# #         return gcd(m,n%m)
# #
# # print(gcd(48,18))
# #
# # import math
# # print(math.factorial(3))
# #
# #
# # Virus_composition=input()
# # c=set(Virus_composition)
# # n=int(input())
# # a=[]
# # for i in range(n):
# #     m=input()
# #     a.append(m)
# #
# # for x in range(0,len(i)):
# #     if x in c:
# #         print("POSITIVE")
# #
# #
# # x='fjyjkyukyg'
# # print('u'in x)
#
# # import sys
#
# # max_int = sys.maxint
# # min_int = sys.maxint - 1
# # long_int = sys.maxint + 1
# #
# # print("maxint :" + str(max_int) + " - " + str(type(max_int)))
# # print("maxint - 1 :" + str(max_int) + " - " + str(type(min_int)))
# # print("maxint + 1 :" + str(max_int) + " - " + str(type(long_int)))
#
# # def solve(A):
# #     Prefixsum = []
# #     Prefixsum.append(A[0])
# #     for i in range(1, len(A)):
# #
# #         Prefixsum.append(Prefixsum[i - 1] + A[i])
# #     for k in range(1, len(Prefixsum)):
# #         if Prefixsum[k - 1] == Prefixsum[(len(Prefixsum) - 1)] - Prefixsum[k]:
# #             return k
# #     else:
# #         return -1
# #
# # print(solve([-7, 1, 5, 2, -4, 3, 0]))
# # for i in range(5):
# #     for k in range(5):
# #         print("*",end=" ")
# #     print( )
# def solve(A):
#     count=0
#     PrefixSumEven=[]
#     PrefixSumOdd=[]
#     PrefixSumEven.append(A[0])
#     PrefixSumOdd.append(0)
#     for i in range(1,len(A)):
#         if i%2!=0:
#             PrefixSumEven.append(PrefixSumEven[len(PrefixSumEven)-1])
#             PrefixSumOdd.append(PrefixSumOdd[len(PrefixSumOdd)-1]+A[i])
#         else:
#             PrefixSumEven.append(PrefixSumEven[len(PrefixSumEven) - 1]+A[i])
#             PrefixSumOdd.append(PrefixSumOdd[len(PrefixSumOdd)-1])
#     if PrefixSumOdd[-1]-PrefixSumOdd[0]==PrefixSumEven[-1]-PrefixSumEven[0]:
#         print(0)
#     for k in range(1,len(A)):
#         if PrefixSumEven[k-1]+(PrefixSumOdd[(len(A)-1)]-PrefixSumOdd[k])==PrefixSumOdd[k-1]+PrefixSumEven[(len(A)-1)]-PrefixSumEven[k]:
#             print(k)
#
#
#     print(PrefixSumEven)
#     print(PrefixSumOdd)
#
#
# def solve(A, B):
#     for i in range(1, len(A)):
#         A[i] = A[i - 1] + A[i]
#     max = A[B - 1]
#     if A[-1] - A[-B - 1] > max:
#         max = A[-1] - A[-B - 1]
#
#     for k in range(1, B):
#         if A[B - k - 1] + (A[-1] - A[-1 - k]) > max:
#             max = A[B - 1 - k] + A[-1] - A[-1 - k]
#     return max
#
# def rangeSum( A, B):
#     Ans = []
#     Prefixsum = []
#     Prefixsum.append(A[0])
#     for i in range(1, len(A)):
#         Prefixsum.append(Prefixsum[i - 1] + A[i])
#     Prefixsum.insert(0,0)
#     print(Prefixsum)
#     for k in B:
#         a = k[0]
#         b = k[1]
#         print(a)
#         print(b)
#         Ans.append(Prefixsum[b] - Prefixsum[a-1])
#     return Ans
#
# def solve(A):
#     Prefixsum = []
#     Prefixsum.append(A[0])
#     for i in range(1, len(A)):
#         Prefixsum.append(Prefixsum[i-1] + A[i])
#     a=max(A)
#     prod=(a*len(A))-Prefixsum[-1]
#     return prod
#
# def solve(A):
#     Prefixsum = []
#     Ans = []
#     Prefixsum.append(A[0])
#     for i in range(1, len(A)):
#         Prefixsum.append(Prefixsum[i - 1] * A[i])
#     print(Prefixsum[-1])
#     for k in A:
#         Ans.append(Prefixsum[-1] // k)
#     return Ans
# print(solve([1, 2, 3, 4, 5]))
a="128"
b="100"
# # sum1=int(a,2)+int(b,2)
# print(int(a,2))
# print(int(a,10))
# print(bin(int(a,2)+int(b,2)))
# # print(help(int))
# print(bin(int(a,2)+int(b,2)))
# A=(bin(int(a)))
# B=A[2:]
# print(A)
# print(B)
# count=0
# for k in range(len(B)):
#     if B[k]=="1":
#         count+=1
# print(count)
# def numSetBits(A):
#     B = bin(int(A))
#     count = 0
#     for k in range(2, len(B)):
#         if B[k] == "1":
#             count += 1
#     return count
#
# print(numSetBits(128))
# a="3"
# b=str(bin(a))
# a=a.zfill(32)
# print(a)
# def reverse(A):
#     B = bin(A)
#     B=B[2:]
#     B = str(B)
#     # print(B)
#     B = B.zfill(32)
#     # print(B)
#     B=B[::-1]
#     # print(B)
#     return int(B, 2)
# print(reverse(3))
# print((9^17))

# c="kslauik"
# print(c[::-1])
# def cla1(A):
#     s=0
#     for k in A:
#         s=s^k
#     # if s%2==0:
#     #     return 1
#     # else:
#     return s
# #
# print(cla1([1, 2, 3, 1, 2, 4]))
# def clas1(A):
#     Q=A.count("1")
#
#     totalsum=0
#     q = len(A)
#     for i in range(q):
#         leftcount = 0
#         rightcount = 0
#         if A[i]=="0":
#             for k in range(i-1,-1,-1):
#                 if A[k]=="1":
#                     leftcount+=1
#                 else:
#                     break
#
#             for l in range(i+1,q):
#                 if A[l]=="1":
#                     rightcount+=1
#                 else:
#                     break
#         if leftcount+rightcount<Q:
#             totalsum = max(totalsum, leftcount + rightcount + 1)
#         else:
#             totalsum=leftcount+rightcount
#     return totalsum
#
# print(clas1("010100110101"))
# A=[5, 6, -1, 7, 8]
# for i in range(len(A)):
#     start=0
#     end=0
#     if A[i]>0:
#         # length+=1
#         for k in range(i+1):
#
# A = [1, 6, 4, 2, 6, 9]
# s=[]
# for i in range(1,len(A)):
#     for k in range(i-1,-1,-1):
#         if A[k]<A[i]:
#             s.append([])
# import sys
# c=sys.intmax
# print(c)
# import sys
# print(sys.int_info)
# A = [1, 6, 4, 2, 6, 9]
# B = [2, 5, 7, 3, 2, 7]
# A = [ 2, 4, 5, 4, 10 ]
# B = [ 40, 30, 20, 10, 40 ]
# A = [ 1, 3, 5 ]
# B = [ 1, 2, 3 ]
# n = len(A)
# mincost = 9999999999
# flag = False
# for q in range(1, n):
#     cost = 0
#     minB1 = 9999999999
#     minB2 = 9999999999
#     for p in range(0, q):
#         if (A[p] < A[q]):
#             falg = True
#             minB1 = min(minB1, B[p])
#     for r in range(q + 1, n):
#         if (A[q] < A[r]):
#             minB2 = min(minB2, B[r])
#     if minB1 == 9999999999 and minB2 == 9999999999:
#         pass
#     else:
#         cost = minB1 + B[q] + minB2
#
#     mincost = min(mincost, cost)
# if flag == False:
#     print("-1")
# if mincost == 9999999999:
#     print("-1")
# else:
#     print(mincost)
# A=[1,2,7,0,3,5,-4,-3,2,-1]
# result=[]
# for i in range(len(A)):
#     s=[]
#     if A[i]>=0:
#         for k in range(i,len(A)):
#             if A[k]>=0:
#                 s.append(A[k])
#             else:
#                 break
#         if len(s)>len(result):
#             result=s
# print(result)
# def pypart2(n):
#     # number of spaces
#     k = 2 * n
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end=" ")
#
#         # decrementing k after each loop
#         k = k - 2
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing stars
#             print("* ", end="")
#
#         # ending line after each row
#         print("\r")


# Driver Code
# n = 5
# pypart2(n)
# N=4
# for i in range(N):
#     for k in range(N-i):
#         print("*",end=" ")
#
#     for n in range(i):
#         print(" ",end=" ")
#     for n in range(i):
#         print(" ",end=" ")
#     for l in range(N-i):
#         print("*",end=" ")
#
#
#     print()
# for mi in range(N):
#     for st in range(mi+1):
#         print("*",end=" ")
#     for kl in range(N-mi-1):
#         print(" ",end=" ")
#     for kl in range(N-mi-1):
#         print(" ",end=" ")
#     for sd in range(mi+1):
#         print("*",end=" ")
#
#     print()
# ni=4
# for i in range(ni):
#     for k in range(ni-i):
#         print("*",end=" ")
#     for n in range(i):
#         print(" ",end=" ")
#     for n in range(i):
#         print(" ",end=" ")
#     for l in range(ni-i):
#         print("*",end=" ")
#
#
#     print()
#     for mi in range(ni):
#         for st in range(mi+1):
#             print("*",end=" ")
#         for kl in range(ni-mi-1):
#             print(" ",end=" ")
#         for kl in range(ni-mi-1):
#             print(" ",end=" ")
#         for sd in range(mi+1):
#             print("*",end=" ")
#
#         print()
# a=5
# print(a>>3)
# import time
# start=time.time()
# print(start)
# s=[]
#
# for i in A:
#     if i in s:
#         s.remove(i)
#     else:
#         s.append(i)
# print(s)
# end=time.time()
# print(end)
# print(end-start)
# xor=42^54
# print(xor)
# x=xor&~(xor-1)
# print(x)
# print(bin(x))
# x,y=0,0
# xor=0
# A=[1,2,3,4,3,1]
# for i in A:
#     xor=xor^i
# right_bit=xor&~(xor-1)
# print(right_bit)
# for i in A:
#     if (i&right_bit):
#         print(x,end=" ")
#         x=x^i
#
#     else:
#         print(y,end=" ")
#         y=y^i

# from functools import reduce

# print(x,y)

# xor=28
# print(xor&~(xor-1))
# print(10&20&15&4)
# print(20&15&8&14)
# a=[20,15,4,10]
# print(max([reduce(lambda x,y:x&y,a)]))
# d=max([reduce(lambda x,y: x&y , a]))
# print(d)
# a=list(map(lambda x:bin(int(x))[2:],input().split()))
# print(a)
# k=max(len(i) for i in a)
# b=[i.zfill(k) for i in a]
# a=b
# print(a)
# for i in range(len(a)):
#     a[i]=(k-len(a[i]))*"0"+a[i]
# s,m=[],list(range(len(a)))
# for i in range(k):
#     if [g[i] for g in a].count("1")>=4:
#         l=[]
#         for j in range(len(a)):
#             if j in m:
#                 if a[j][i]=="1":
#                     l.append(j)
#         if len(l)>=4:
#             a.append("1")
#         else:
#             s.append("0")
#         m=l
#     else:
#         s.append("0")
# s.reverse()
# print(sum(list(map(lambda x,y:(2**y)*int(x),s,range(len(s))))))
# a=list(map(lambda x:bin(int(x))[2:],input().split()))
# # print("input a:",a)
# k=max(len(i) for i in a)
# # print(k)
# a=list(i.zfill(k) for i in a)
# print("a after refillment:",a)
# # lg=list(range(len(a)))
# # print(lg)
# l=[]
# for i in range(k):
#     count=0
#     for k in a:
#         if k[i]=="1":
#             count+=1
#     if count>=4:
#         l.append("1")
#         for k in a:
#             if k[i]=="0":
#                 a.remove(k)
#             # if len(a)==4:
#             #     j = "".join(l)
#             #     print(int(j, 2))
#     else:
#         l.append("0")
# # print("LG:",lg)
# print("l:",l)
# j="".join(l)
# print(type(j))
# print(int(j,2))

# C="ABCD"
# sum=0
# for i in range(len(C)-1,-1,-1):
#     a=(ord(C[i])-64)*(26**(len(C)-(i+1)))
#     sum=sum+a
# print(sum)

#
# def solve(A,B):
#
#         return abs(A-B)
#
# print(solve(1,2))
# import math
# print(math.gcd(10,5))
# a="48"
# ai=int(a[0])%8
# for i in range(1,len(a)):
#         s=(ai*10+int(a[i]))%8
#         ai=s
#         st=s%8
# if st==0:
#         print("1")
# else:
#         print("0")
#
#
# import math
# print(math.lcm(4,6))

# help(eval("10"))

# a="AA"
# class ags:
#     def gcd(self,a,b):
#         if b==1:
#             return a
#         else:
#             y=self.gcd(b,a%b)
#
#
#         return int((a*b)/y)
# t1=ags()
# print(t1.gcd(9,18))
# class Solution():
#     def LCM1(self,A,B,org_A,org_B):
#         if B == 0:
#             return A
#         else:
#             y=self.LCM1(B,B%A,org_A,org_B)
#         return y
#         return ((org_B*org_A)//y)
#
#     def LCM(self,A,B):
#         return self.LCM1(A,B,A,B)
# t=Solution()
# print(t.LCM(3,9))
# def solve(A):
#     if A % 4 == 0:
#         if A % 100!= 0:
#             return "1"
#         else:
#             return "0"
#     else:
#         return "0"
#
#
# print(solve(2020))
# A=[1,2,2,3,4,5,3,3,2,1,4,3,3,3]
# a={}
# for i in A:
#     if a.get(i) is None:
#         a[i]=1
#     else:
#         a[i]+=1
# # print(a)
# a=["3","30","34","5","9"]
# a.sort(key=lambda x:x[0],reverse=True)
# print(a)
# print("".join(a))
# import functools
# a.sort(key=)
# A = [0 ,1, 2 ,0, 1, 2]
# # A.sort()
# print(sorted(A))
# print(A)
# A = [ 5, 6, 2 ]
# A.sort()
# print(A)
# greatest_count=1
# if A[-1]==0:
#     print("1")
# for i in range(len(A)-2,-1,-1):
#     if A[i]!=A[i+1]:
#         greatest_count+=1
#

# A=[1,4,2]
# A.sort()
# k=A[1]-A[0]
# for i in range(1,len(A)):
#     if abs(A[i]-A[i-1])!=k:
#         print("0")
#         break
# else:
#     print("1")

# a=[1,46,7,8,9,6,5,4,4,0]
# a.sort()
# b=a
# print(b,a)


# k=[0,1,2]
# def grade(n):
#     if n==1 or n==2:
#         return n
#     else:
#         for i in range(3,n+1):
#             k.append(grade(n-1)+grade(n-2))
#     return k[-1]
# print(grade(10))
#
#
# print(k)
# nums=list(map(int,input().split()))
# k=int(input())
# if k > 0:
#     for i in range(k):
#         sd = nums[-1]
#         nums.pop(-1)
#         nums.insert(0,sd)
# else:
#     for i in range(0,k,-1):
#         sd = nums[0]
#         nums.pop(0)
#         nums.insert(-1,sd)

# print(nums)
# a=eval(input("enter a"))
# print(type(a))
# dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# a=input()
# a=list(a)
# li=list(map(int,a))
# k=[]
# for i in li:
#     k.append(list(dict[i]))
# # print("k",k)
# while len(k)>1:
#     a=k.pop()
#     b=k.pop()
#     k1=[str(i1)+str(i2) for i1 in a for i2 in b]
#     # print("k1",k1)
#     # ji=["".join(i) for i in k1]
#     k.append(k1)
# print(k[0])
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.left=b
a.right=d
b.left=c
c.left=e

def dfs(root,k):
    print(k)
    if root is None:
        return
    if(root.left is None and root.right is None):
        print(sum(k)+root.val)
        return
    dfs(root.left,k.append(root.val))
    dfs(root.right,k.append(root.val))
dfs(a,[])



def sum(a, b):
    return a+b;

def sum1(a,b):
    print(a+b)

print(sum1(2,3))
print(sum(2,3))