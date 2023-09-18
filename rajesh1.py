# print(~12)
# print(12&13)
# print(12|13)
# print(12^13)
# print(12<<13)
# print(10<<2)
# num =int(input("enter a number:"))
# if (num % 2)==0:
#     print("the number is even")
# else:
#     print("the number is odd")
# list=[10,34,28,90,65,3,9]
# for  num in list:
#     if num %2==0:
#         print(num,end="")
# import math
# x =math.sqrt(25)
# print(x)
# x =math.sqrt(35)
# print(x)
# print(math.floor(2.6))
# print(math.ceil(2.6))
# print(3**2)
# print(math.pow(3,2))
# print(math.pi)
# print(math.e)
# import math as m
# print(m.sqrt(25))
# print(m.floor(2.9))
# from math import pow,sqrt
# print(pow(4,5))
# print(sqrt(25))
# help('math')
# x=7
# r=x%2
# if r==0:
#     print("even")
#     if x>5:
#         print("great")
#     else:
#         print("Not so great")
# else:
#     print("odd")
# print("bye")
# x=2
# if x==1:
#     print("one")
# elif(x==2):
#     print("two")
# elif(x==3):
#     print("three")
# elif(x==4):
#     print("four")
# x=1
# while loop
# while x<=5:
#     print("rajesh",end='')
#     j=1
#     while j<=4:
#         print("reddy",end='')
#         j=j+1
#     x=x+1
#     print()
# for loop
# x="rajesh"
# for i in x:
#     print(i)
# x=int(input("how many candies you wan"))
# i=1
# while i<=x:
#     print("candy")
# from array import *
# arr = array('i',[])
# n=int(input("enter the length of the array"))
# for i in range(n):
#     x=int(input("enter the next value"))
#     arr.append(x)
# print(arr)
# val =int(input("enter the value of search"))
# k = 0
# for e in arr:
#     if e==val:rq
#         print(k)
#         break
#     k+=1
#     print(arr.index(va
# print("rajesh")

# class Solution:
#     def minTaps(self, n,ranges) -> int:
#         target=111_11_11
#         def dfs(index,number):
#             if index==len(ranges):
#                 return float("inf")
#             if number==target:
#                 return 0
#
#             #not pick
#             notpick=dfs(index+1,number)
#
#             pick=0
#
#
# s1=Solution()
# print(s1.minTaps(5,[3,4,1,1,0,0]))

# def function(arr):
#     even=[]
#     odd=[]
#     for i in arr:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even+odd
# num=int(input("enter a value"))
# if (num%2)==0:
#     print("the number is even")
# else:
#     print("the number is odd")
# list=[23,42,53,65,76]
# for num in list:
#     if num%2 ==0:
#         even_count +=1
#     else:
#         odd_count +# print("even number in the list" even_count)
# print("odd number in the list",odd_count)

# x=10
# y=34
# def add(x,y):
#     return(x+y)
# def subtract(x,y):
#     return(x-y)
# import math as mt
# print(mt.sqrt(16))
# print(mt.factorial(6))
# def add(a,b):
#     result=a+b
#     return result
# print(m.p



######   QUICK SORT   ######
# arr=[0,0,0,0,0,0,0]
# def qs(arr,low,high):
#     def func(arr,low,high):
#         pivot=arr[high]
#         index=low
#         for i in range(low,high+1):
#             if arr[i]<=pivot:
#                 arr[i],arr[index]=arr[index],arr[i]
#                 index+=1
#         return index-1
#     if low<high:
#         pindex=func(arr,low,high)
#         qs(arr,low,pindex-1)
#         qs(arr,pindex+1,high)
#     return arr
#
# print(qs(arr,0,len(arr)-1))


# from collections import Counter
# def minDeletions(s) -> int:
#     def dfs(index,dictionary):
#         if index==-1:
#             return float("inf")
#
#         temp=dictionary.values()
#         l=len(temp)
#         k=len(set(temp))
#         if l==k:
#             return 0
#
#         pick1=dfs(index-1,dictionary)
#         # print(id(dictionary))
#         dictionary[s[index]]-=1
#         if dictionary[s[index]]==0:
#             del dictionary[s[index]]
#         pick2=1+dfs(index-1,dictionary)
#         if s[index] in dictionary:
#             dictionary[s[index]]+=1
#         else:
#             dictionary[s[index]]=1
#         return min(pick1,pick2)
#     return dfs(len(s)-1,Counter(s))
# print(minDeletions("aaabbbcc"))

