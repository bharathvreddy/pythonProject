# from array import *
# arr=array('i',[1,2,3,4,5,6])
# for i in arr:
#     print(i)
# print("step 2")
# print(arr[1])
# arr.append(6)
# arr.insert(2,54)
# mn=[58,5,554]
# arr.extend(mn)
# print(arr)
# a=["kjasu","jhus","jkagusiia"]
# a.sort(key=lambda x : len(x))
# print(a)
# s="{[]}"
# a=[]
# open_list=["(","[","{"]
# closed_list=[")","]","}"]
# def raj(s):
#     if len(s)==0:
#         return True
#
#     for i in s:
#         if i in open_list:
#             a.append(i)
#         elif i in closed_list:
#             b=closed_list.index(i)
#             if a[len(a)-1]!=open_list[b]:
#                 return False
#             else:
#                 a.pop(len(a)-1)
#     if a==[]:
#         return True
#     else:
#         return False


# s="GUGPUAGAFQBMPYAGGAAOALAELGGGAOGLGEGZ"
# A_count=0
# res=0
# for i in range(len(s)):
#     # print(s[i],end="")
#     if s[i]=="A":
#         A_count+=1
#     if s[i]=="G":
#         res+=A_count
# # print(res)
#
# a=[93,57,83,41,100,10,79,27,94,22, 4, 96, 48, 18, 89, 37, 21, 5, 46, 81, 15, 30, 47, 23, 34, 65, 55, 9, 36, 20, 54, 17, 7, 56, 78, 84, 87, 97, 16, 69, 28, 11, 44, 49, 8, 25, 98, 75, 53, 62, 19, 24, 80, 68, 50, 91, 1, 86, 77, 14, 72, 66, 42, 63, 73, 45, 31, 61, 85, 64, 35, 32, 92, 71, 74, 3, 99, 52, 90, 43, 6, 40, 38, 2, 12, 59, 29, 82, 76, 60, 67, 13, 70, 58, 39, 33, 95, 88, 51, 26 ]
# bigger=a[len(a)-1]
# count=1
# s=[bigger]
# for i in range(len(a)-2,-1,-1):
#     if a[i]>bigger:
#         count+=1
#         bigger=a[i]
#         s.append(bigger)
# print(s)
# a=[16,17,17,4,3,5,2]
# min1=a[0]
# max=a[0]
# if min1==max:
#     print("1")
# for i in a:
#     if i<min1:
#         min1=i
#     if i>max:
#         max=i
# min_index=-1
# max_index=-1
# len=len(a)
# for k in a:
#     if k==min1:
#         min_index=a.index(k)
#     if k==max:
#         max_index=a.index(k)
#     k=max_index-min_index
#     st=min(len,k)
#     if st<0:
#         st=st*-1
# # k=[1,0,1,0,0,1,1,0]
# press_count=0
# for j in k:
#     if press_count%2==0:
#         if j==0:
#             press_count+=1
#         # else:
#         #     press_count+=0
#     else:
#         if j==1:
#             press_count+=1

# print(press_count)
# a=[1,2,3,4,5,6,7,8,9,5,2,65,6,2,5,6]
#
# d=a[9:]
# d.sort()
# a[9:]=d
# print(a)
# a="asdfgh"
# print(bool(a[10] is None))
#list(map(int,input().split()))
#list(map(int,input().split()))
#n=
# print((2+3)//2)
#burger problem sent by siseendri
# n=int(input())
# k=list(map(int,input().split()))
# capacity=list(map(int,input().split()))
# sum1=0
# for i in range(len(capacity)):
#     available=k[i]+k[i+1]
#     if available >= capacity[i]:
#         if k[i]>=capacity[i]:
#             k[i]-=capacity[i]
#             sum1+=capacity[i]
#         else:
#
#             k[i+1]=k[i+1]-(capacity[i]-k[i])
#             k[i]=0
#             sum1+=capacity[i]
#     else:
#         sum1+=available
#         k[i]=0
#         k[i+1]=0
# print(sum1)
# print(k)
# #voters problem
# k=[[0,2],[1,4],[3,6]]
# y_supporters=0
# for x in k:
#     y_supporters+=x[0]
# totalpeople=[x[0]+x[1] for x in k]
# print(totalpeople)
# n=0
# x_supporters=0
# while 1:
#     maxpeople=max(totalpeople)
#     maxpeople_index = totalpeople.index(maxpeople)
#     totalpeople.remove(maxpeople)
#     x_supporters+=maxpeople
#     y_supporters-=k[maxpeople_index][0]
#     if  x_supporters>y_supporters:
#         n+=1
#         break
#     else:
#         n+=1

# print(n)
# from sketchpy import library as lb
# lb.rdj().draw()

# dict={}
# dict[None1]=0
# print(dict)
# class raj:
#     count=0
#     # def __init__(self):
#     #     raj.count+=1
#     # @classmethod
#     # def getob(cls):
#     #     print(raj.count)
#     @staticmethod
#     def staticmethod():
#         print("hi")

# class Solution:
#     def f(self):
#         def prob(index,nums):
#             if index==len(nums)-1:
#                 return True
#             for i in range(nums[index]):
#                 if prob(index+i+1,nums)==True:
#                     return True
#             return False
#         prob(0,[2,3,1,1,4])
# S=Solution()
# print(S.f())
# def f():
#     a=[3,2,1,0,0]
#     r=0
#     list=[0]
#     while r<len(a)-1:
#         if r<len(a)-1 and len(list)==0:
#             return False
#         j=list.pop(0)
#         for k in range(1,a[j]+1):
#             list.append(j+k)
#             r=max(r,k+j)
#     return True
# print(f())
# def raj(array):
#     k=1
#     for i in range(len(array)-2,-1,-1):
#         if array[i]>=k:
#             k=1
#         else:
#             k+=1
#     if array[0]<k:
#         return False
#     else:
#         return True
# print(raj([3,2,1,1,0]))

