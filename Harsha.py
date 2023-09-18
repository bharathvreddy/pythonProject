# V=int(input("Enter no of vehicles:"))
# W=int(input("Enter no of wheels:"))
#
# lst=[(x,y) for x in range(int(W/2)) for y in range(int(W/2)) if int(x*2)+(y*4)==W and x+y==V ]
# print("No. of bikes and cars respectively:")
# # for z in range(len(lst)):
# #     print(z,lst[z])
#
#
#
# #Binary heap tree
#
# class Bheaptree:
#     def __init__(self,size):
#         self.size=size
#         self.list= (size+1) * [None]
#         self.heapsize=0
#     def heapify(self,index,heaptype):
#         parent=int(index/2)
#         if index<=1:   #index value decreases ,and atmost it can reach 1,not morethan that
#             return
#         if heaptype=="min":
#             if self.list[parent]>self.list[index]:
#                 temp=self.list[index]
#                 self.list[index]=self.list[parent]
#                 self.list[parent]=temp
#                 self.heapify(parent, heaptype)
#         if heaptype=="max":
#             if self.list[parent]<self.list[index]:
#                 temp=self.list[index]
#                 self.list[index]=self.list[parent]
#     #             self.list[parent]=temp
#     #             self.heapify(parent, heaptype)
#     #
#     #
#     #
#     #
#     # def insert(self,nodevalue,heaptype):
#     #     if self.heapsize==self.size:
#     #         return "Tree is full"
#     #     else:
#     #         self.list[self.heapsize+1]=nodevalue
#     #         self.heapsize+=1
#     #         self.heapify(self.heapsize,heaptype)
#     #
#     # def delete(self,heaptype,index=1):
#     #     currentindex=1
#     #     leftchild=(currentindex*2)
#     #     rightchild=(currentindex*2)+1
#     #
#     #     if heaptype=="min":
#     #         if leftchild!=None and rightchild!=None:
#     #             if leftchild < rightchild:
#     #                 a = leftchild
#     #             else:
#     #                 a = rightchild
#     #             self.list[currentindex]=a
#     #             b=self.list.index(a)
#     #             self.delete(b,heaptype)
#     #         if leftchild!=None and rightchild==None:
#     #             if self.list[currentindex]
#     #
#     #
#
#
#
#
# #
# # heap=Bheaptree(8)
# # heap.insert(10,"max")
# # heap.insert(3,"max")
# # heap.insert(1,"max")
# # print(heap.list)
#
#
#
# #GRAPHS
# class Graphs:
#     def __init__(self,dict):
    #     self.dict=dict
    # def addvertex(self,vertex,edge):
    #     self.dict[vertex].append(edge)
    # def bfs(self,vertex):
    #     visited=[vertex]
    #     queue=[vertex]
    #     while queue:
    #         devertex=queue.pop(0)     #for dfs devertex=queue.pop()  i.e.,pop out the element which has been inserted at last
    #         print(devertex)
#             for adjacentvertex in self.dict[devertex]:
#                 if adjacentvertex not in visited:
#                     visited.append(adjacentvertex)
#                     queue.append(adjacentvertex)
#
#
# Dict={"a":["d","b"],
#       "b":["a","e","c"],
#       "c":["b","f"],
#       "d":["a","e","g"],
#       "e":["b","f","g","d"],
#       "f":["c","g","e"],
#       "g":["d","e","f"]
#     }
#
# graphs=Graphs(Dict)
# graphs.bfs("a")
#
#
# def raj(a,b):
#     return a+b
#
# def raj(a,b,c):
#     return a+b+c
#
#
# print(raj(2,5,7))
#
# l=[]
# for i in range(6):
#     l.append(list(map(int,input().split())))
# print(l[0][1][1])
#

# import os
# env_var=os.environ
# print(env_var)

# a=",,,,,rrttgg....reddy...rrr"
# print(a.strip(",.rtg"))
# fptr = open(os.environ['OUTPUT_PATH'], 'w')
# a=input("Enter:").rstrip().split()
# # print(a)
#
# a=list(map(int,input("Enter numbers").split()))
# # print(a)
# res=1
# cos=1
# b=[]
# for i in a:
#     if i>0:
#         res=res*i
#     if i<0:
#         b.append(i)
# # print("res",res)
# if len(b)%2==0:
#     for i in b:
#         cos=cos*i
# if len(b)%2!=0:
#     b.sort()
#     for k in range(len(b)-1):
#         cos=cos*b[k]
#
# total=res*cos
# a=[1,2,3,4,5,6,7,8]
# rot=3
# i=0
# j=rot
# while(i<j):
#     a[i],a[j]=a[j],a[i]
#     i=i+1
#     j=j-1
# print(a)
#

# def solve(A):
#     min_index = 0
#     max_index = 0
#     min1 = A[0]
#     max1 = A[0]
#     for i in A:
#         if i < min1:
#             min1 = i
#             min_index = A.index(min1)
#         if i > max1:
#             max1 = i
#             max_index = A.index(max1)
#     length=min_index-max_index
#     if length<0:
#         length*=-1
#     length+=1
    # print(min1,max1,min_index,max_index)
    #
    # for k in range(len(A)):
    #     if A[k] == min1:
    #         min_index =k
    #     if A[k] == max1:
    #         max_index =k
    #     fr = (min_index - max_index)
    #     if fr<0:
    #         fr*=-1
    #     frs=fr+1
    #     length = min(length, frs)
    # return length


# s="pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"
# s="AbEc"
# # print(len(s))
# n=0
# l=["A","a","e","E","i","I","O","o","U","u"]
# for i in range(len(s)):
#     if s[i] in l:
#         k=(len(s)-i)
#         n=n+k
# print(n%10003)

# count = 1
#
# max1 = A[-1]
# s = [max1]
# for k in range(len(A) - 2, -1, -1):
#     if A[k] > max1:
#         s.append(A[k])
#         max = A[k]
# print(s)
# a=[ 28, 71, 83, 33, 3, 84, 47, 26, 65, 90, 27, 63, 39, 6, 79, 73, 25, 80, 5, 61, 56, 42, 30, 31, 45, 7, 76, 55, 24, 52, 34, 60, 68, 44,  9, 2, 22, 48, 37, 38, 14, 20, 17, 77, 12, 4, 29, 64, 81, 21, 59, 13, 18, 35, 78, 50, 89, 16, 75, 46, 69, 8, 86, 87, 49, 70, 43, 85, 32, 72, 67, 10, 41, 58, 1, 15, 11, 40, 54, 23, 36, 19, 53, 66, 51, 88, 82, 62, 74, 57 ]
# bigger=a[len(a)-1]
# # count=1
# s=[]
# s.append(bigger)
# for i in range(len(a)-2,-1,-1):
#     if a[i]>bigger:
#         # count+=1
#         bigger=a[i]
#         s.append(bigger)
# k=list(map(str,s))
# print(" ".join(k))

# A  = [-2,-1,-1,-1,56,-3,-24]
# sum =A[0]
# for i in range(1, len(A)):
#     if A[i-1] > 0:
#         A[i] = A[i] + A[i-1]
# # print(A,A[i])
# # max = A[0]
# # for i in A:
# #     if i > max:]
# #         max = i
# # print(max)
# A=[15,7,11,7,9,8,18,1,16,18,6,1,1,4,18]
# # A=[3, 7, 90, 20, 10, 50, 40]
# # A=[3, 7, 5, 20, -10, 0, 12]
# B=6
# c=[A[0]]
# if B==1:
#     print(A.index(min(A)))
# for i in range(1,len(A)):
#     s=c[i-1]+A[i]
#     c.append(s)
# print(c)
# min_sum=c[B-1]
# ind=0
# # print(min_sum)
# for k in range(B,len(A)):
#     l=c[k]-c[k-B]
#     if l<min_sum:
#         min_sum=l
#         ind=k-B+1
# print(ind)
# C = [2, 1, 3, 4, 5]
# B=12
# max1=C[0]
# for i in range(1,len(C)):
#     if C[i]>0:
#         C[i]=C[i-1]+C[i]
#     print(C)
#     if C[i]>max1 and C[i]<B:
#         max1=C[i]
#         if C[i]==B:
#             print(B)
# print(max1)
# A=[1,2,3,4,5,6]
# B=[1,2,3,4,5,6]
# C = list(map(lambda x,y:x+y,A,B))
# print(C)
# A = 5
# B = 12
# C = [2, 1, 3, 4, 5]
# max1=C[0]
# for i in range(1,len(C)):
#     if C[i]>0:
#         C[i]=C[i-1]+C[i]
# print(C)
#             # if C[i]>max1 and C[i]<B:
#             #     max1=C[i]
#                 # if C[i]==B:
#                 #     return B
# if B>C[-1]:
#     print("0")
# else:
#     for k in range(len(C)-1,-1,-1):
#         if C[k]<=B:
#             print(C[k])
#             break
# s=0
# A = 5
# B = 12


# def nextGreaterElement(n: int) -> int:
#     digits = list(str(n))
#     print(digits)
#     i = len(digits) - 1
#     print(i)a= list(str(n))
#     j=set(a)
#     if len(j)==1:
#         return -1
#     print(a)
#     if len(a) == 2 and a[0] >= a[1]:
#         return -1
#     if len(a)==2 and a[0]<a[1]:
#         return "".join([a[1], a[0]])
#     for i in range(len(a) - 1, -1, -1):
#         if a[i-1] >= a[i]:
#             continue
#         else:
#             break
#     # print("i:",i)
#     if i==0:
#         return -1
#     print("a1:",a[i-1])
#     # f=a.index(min(a[i:]),i,len(a))
#     # a[i-1],a[f]=a[f],a[i-1]
#     d = a[i-1:]
#     print("d:",d)
#     d.sort()
#     print("sorted d:", d)
#     ij=d.index(a[i-1])
#     print("ij:",ij)
#     for ik in range(len(d)):
#         if d[ik]>a[i-1]:
#             ijk=ik
#             break
#     print("ijk is :",ijk)
#     d[0],d[ijk]=d[ijk],d[0]
#     print("d:",d)
#     dgf=d[1:]
#     print("jhsgag:",dgf)
#     dgf.sort()
#     d[1:]=dgf
#     print("d is",d)
#     a[i-1:] = d
#     print(a)
#     k=int("".join(a))
#     print("k:",k)
#     if k>=2147483648:
#         return -1
#     else:
#         return k
#     while i - 1 >= 0 and digits[i] <= digits[i - 1]:
#         i -= 1
#     print(i)
#     if i == 0: return -1
#
#     j = i
#     while j + 1 < len(digits) and digits[j + 1] > digits[i - 1]:
#         j += 1
#
#     digits[i - 1], digits[j] = digits[j], digits[i - 1]
#     digits[i:] = digits[i:][::-1]
#     ret = int(''.join(digits))
#
#     return ret if ret < 1 << 31 else -1
# print(nextGreaterElement(8192))



# a=12
# a=list(str(a))
# # print(a)
# for i in range(len(a)-1,0,-1):
#     if a[i-1]>a[i]:
#         continue
#     else:
#         break
# print(i)
# if i==-1:
#     print("-1")
# while(i<len(a)):
#     # print("i:",i)
#     # s=a.index(min(a[i:]))
#     # print("/s:",s)
#     # print(a[s])
#     a[i-1],a[len(a)-1]=a[len(a)-1],a[i-1]
#     # print(a)
#     i+=1
# print("".join(a))
# s=0
# for i in range(32):
#     s=s+(2**i)
# print("s:",s)
# def k(n):
#     a= list(str(n))
#     j=set(a)
#     if len(j)==1:
#         return -1
#     print(a)
#     if len(a) == 2 and a[0] >= a[1]:
#         return -1
#     if len(a)==2 and a[0]<a[1]:
#         return "".join([a[1], a[0]])
#     for i in range(len(a) - 1, -1, -1):
#         if a[i-1] >= a[i]:
#             continue
#         else:
#             break
#     # print("i:",i)
#     if i==0:
#         return -1
#     print("a1:",a[i-1])
#     # f=a.index(min(a[i:]),i,len(a))
#     # a[i-1],a[f]=a[f],a[i-1]
#     d = a[i-1:]
#     print("d:",d)
#     d.sort()
#     print("sorted d:", d)
#     ij=d.index(a[i-1])
#     print("ij:",ij)
#     for ik in range(len(d)):
#         if d[ik]>a[i-1]:
#             ijk=ik
#             break
#     print("ijk is :",ijk)
#     d[0],d[ijk]=d[ijk],d[0]
#     print("d:",d)
    # dgf=d[1:]
    # print("jhsgag:",dgf)
    # dgf.sort()
    # d[1:]=dgf
    # print("d is",d)
    # a[i-1:] = d
    # print(a)
    # k=int("".join(a))
    # print("k:",k)
    # if k>=2147483648:
    #     return -1
#     else:
#         return k
# class fls:
#     def raj1(self):
#         print("inside raj1")
# l1=fls()
# l2=fls()
# import sys
# res= l1 if sys.getsizeof(l1)> sys.getsizeof(l2) else l2
# print("res is",res)
# res.raj1()

# n=int(input("Enter no. of queens:"))
# col=set()
# posdiag=set()
# negdiag=set()
# res=[]
# board=[["-"]* n]*n
# print(board)
# def backtrack(r):
#     if r==n:
#         copy=[" ".join(row) for row in board]
#         res.append(copy)
#         return
#
#     for c in range(n):
#         if c in col or c+r in posdiag or r-c in negdiag:
#             continue
#
#         col.add(c)
#         posdiag.add(r+c)
#         negdiag.add(r-c)
#         board[r][c]="Q"
#         backtrack(r+1)
#         col.remove(c)
#         posdiag.remove(r+c)
#         negdiag.remove(r-c)
#         board[r][c]="-"
# backtrack(0)
# print(res)


# dict1={}
# def count_letters(S):
#      dict1[str(S[i])]=i+1
#   return dict1
# print(count_letters("The joy of computing python"))
# s="32446656565"
# print(type(s))
# j=int(s)
# print(type(j))
# print(j)
# from itertools import permutations
# a="babad"

# k=["".join(a[i:j]) for i in range(len(a)) for j in range(i+1,len(a)+1) if a[i:j]==a[i:j][::-1]]
# print(k)
# largest_len=len(k[0])
# ans=k[0]
# for i in k:
#     if len(k)>largest_len:
#         largest_len=len(k)
#         ans=i
# print(ans)
#longest palindromic substring
#let s be the input
# res=s[0]
# for i in range(len(s)):
#     #odd length string such as asdfgfdsa or asdfgggfdsa
#     low=i
#     high=i
#     while low>-1 and high<len(s) and s[low]==s[high]:
#         low=low-1
#         high=high+1
#         if high-low+1>len(res):
#             res=s[low:high+1]
#
#    #even length string such as asdffdsa or asffffffffsaaasaja
#    low=i
#    high=i+1
#    while low>-1 and high<len(s) and s[low]==s[high]:
#        low=low-1
#        high=high+1
#        if high-low+1>len(res):
#            res=s[low:high+1]
#     return res

# arr=[1,8,6,2,5,4,8,3,7]
# low=0
# high=len(a)-1
# area=0
# while low<high:
#     area1=(high-low) * min(a[low],a[high])
#     area=max(area1,area)
#     if a[low]>a[high]:
#         high=high-1
#     else:
#         low=low+1
# print(r//ea)
# M=[[1,2,3],[4,5,6],[7,8,1]]
# sum1=0
# i=0
# j=0
# initial=0
# while initial <len(M):
#     sum1+=M[i][j]
#     i+=1
#     j+=1
#     initial+=1
# print(sum1)
#
# sum2=0
# i=len(M)-1
# j=0
# initial=len(M)
# while initial >0:
#     sum2+=M[i][j]
#     i-=1
#     j+=1
#     initial-=1
# print(sum2)
# M=[[1,2,3],[4,5,6],[7,8,1]]
# ki=[]
# for i in range(len(M)):
#     l=[]
#     for k in M:
#         l.append(k[i])
#     ki.append(l)
# print(ki)
# n=int(input())
# starter=0
# for i in range(n):
#     changer = 0
#     for j in range(n):
#         print(starter+changer,end=" ")
#         changer+=4
#     print()
#     starter+=6
# M=[[1,2,3],[4,5,6],[7,8,9],["a","b","c"]]
# i=0

# def printMatrix(array,b):
#     if b is True:
#         for l in array[::-1]:
#             print(l)
#     else:
#         for l in array:
#             print(l)
# for i in range(len(M)):
#     if i%2==0:
#         printMatrix(M[i],True)
#     else:
#         printMatrix(M[i],False)
# a=[1,0,5,2,5,7,8,9,1,5,4]
# minlist=[0]+[a[0]]
# max1=max(a[0],a[1])
# for i in range(1,len(a)-1):
#     max1=max(max1,a[i])
#     minlist.append(max1)
# print(minlist)
# A=[1,0,5,2,5,7,8,9,1,5,4]
# q = [A[0]]
# for i in range(1,len(A)):
#     if A[i] + q[i - 1] > 0:
#         q.append(A[i] + q[i - 1])
#     else:
#         q.append(0)
# print(q)
# print(sum(A))

# #kadane's algorithm
# def maxSubArray(a):
#     if len(a)==1:
#         return a[0]
#
#     q=[a[0]]
#     for i in range(1,len(a)):
#         if q[i-1] > 0:
#             q.append(a[i]+q[i-1])
#         else:
#             q.append(a[i])
#     return max(q)
#
# print(maxSubArray([5,-162,-20,-1]))
#
# B=[[1,2,10],[2,3,20],[2,5,25]]
# A=5
# A=[0]*A
# print(A)
# for i in B:
#     low=i[0]
#     high=i[1]
#     cost=i[-1]
#     for k in range(low-1,high):
#         A[k]+=cost
# print(A)
# A=[1,2,3]
# j=int("".join(A))
# j+=1
# q=list(j)
# print(q)
# A= [0] * A
# for i in B:
#     low=i[0]
#     high=i[1]
#     cost=i[-1]
#     A[low - 1]+=cost
#     if high<len(A):
#         A[high]= A[high] - cost
#     print(A)
# for i in range(1, len(A)):
#     A[i]+=A[i - 1]
# print(A)
#
# A=[1, 0, 5, 2]
# str1=""
# for i in A:
#     str1=str1+str(i)
#     q=int(str1)+1
#     j=list(str(q))
# print(j)
#binary addition
# def raj():
#     A=[ 0, 6, 0, 6, 4, 8, 8, 1 ]
#     q1= A[-1] + 1
#     if q1 > 9:
#         carry=1
#         q1=int(str(q1)[-1])
#     else:
#         carry=0
#     A[-1]=q1
#     for i in range(len(A) - 2, -1, -1):
#         g= A[i] + carry
#         if g>9:
#             carry=1
#             g=int(str(g)[-1])
#         else:
#             carry=0
#         A[i]=g
#     if carry==1:
#         A.insert(0, 1)
#     print(A)
#     i = 0
#     for k in A:
#         if k == 0:
#             i += 1
#         else:
#             break
#     j = A[i:]
#     print(j)
#
# raj()
# A=[]
# if A[0]<0:
# #     A.insert(0,0)
# # for i in A:
# #     if i>0:
# #         low=A.index(i)
# #         high=low
# # res=[]
# # ressum=sum(res)
# # for i in range(1,len(A)):
# #     if A[i]>0:
# #         A[i]=A[i]+A[i-1]
# #     else:
# #         A[i]=0
# # print(max(A))
# a=[1, 2]
# b=[0]
# max1=a[0]
# for i in range(0,len(a)-1):
#     max1=max(a[i],max1)
#     b.append(max1)
# print(b)
# rightmax=[0]
# max1=a[-1]
# for i in range(-1,-len(a),-1):
#     max1=max(a[i],max1)
#     rightmax.insert(0,max1)
# print(rightmax)
# sum1=0
# for i in range(0,len(a)):
#     g=min(b[i],rightmax[i])
#     k=g-a[i]
#     if k>0:
#         sum1+=k
# print(sum1)
# a=[[1,9],[2,3],[4,7]]
# b=[]
# for i in a:
#     for j in i:
#         b.append(j)
# b.sort()
# cat=1
# initial=b[0]
# initial1=0
# for i in a:
#     for j in i:
#         if j==initial:
#             initial1=i[-1]
#             cat=0
#             break
#     if cat==0:
#         break
# print(initial,initial1)
# a=[0,0,1,1,1,2,2,3,3,4]
# i=0
# while i<len(a)-1:
#     j=i
#     while a[i]==a[j+1]:
#         a.pop(j+1)
#         a.insert(j+1,"_")
#         j+=1
#     i=j+1
# print("a1",a)
#dont remove any element, while looping is happening, it wont lead to correct solution
# a=[1,2]
# l=1
# for r in range(1,len(a)):
#     if a[r]!=a[r-1]:
#         a[l]=a[r]
#         l+=1
# print(l)
# k=1
# count=0
# for i in a:
#     if i==k:
#         count+=1
# for i in range(count):
#     a.remove(k)
# print(a)
# for i in range(count):
#     a.append("_")
# print(a)
# ques = "abc"
# n="c"
# for i in range(len(ques)-len(n)+1):
#     if ques[i:i+len(n)]==n:
#         print("found")
#         break
# else:
#     print("not found")
# a=[0,1,2,3,4]
# low=0
# high=len(a)
# target=3
# while 1:
#     if a[(int(low+high)/2)]>target:
#         high=int((low+high)/2)
#     elif a[(int(low+high)/2)]<target:
#         low=int((low+high)/2)
#
#         print(low)
# pos=-1
# high=0
# def func(a,target):
#     low=0
#     high=len(a)-1
#     while low<=high:
#         mid=(low+high)//2
#         if a[mid]==target:
#             return mid
#         else:
#             if a[mid] <target:
#                 low=mid+1
#             else:
#                 high=mid-1
# print(func([1,3,5],1))
# a=[7,1,5,3,6,4]
# max1=a[0]
# for i in a[1:]:
#     max1=max(max1,a[i])
#best time to buy and sell stocks
# def func():
#     a=[6,5,4,3,2,1]
#     if len(a)==1:
#         return 0
#     low = 0
#     high = 0
#     max1 = a[1] - a[0]
#     while high<=len(a)-1 and low<=len(a)-1:
#         max1=max(max1,a[high]-a[low])
#         if a[high]<a[low]:
#             low=high
#         high+=1
#
#
#     if max1 > 0:
#         return max1
#     else:
#         return 0
# print(func())

#binary addition


    #
    #
    # def rst(index, total, ds):
    #     if total == target:
    #         ans.append(ds[:])
    #         return
    #     if index >= len(arr) or total > target:
    #         return
    #
    #     rst(index, total + arr[index], ds + [arr[index]])
    #     rst(index + 1, total, ds)
    #
    # rst(0, 0, [])
    # return ans


def secondSmallest(S, D):
    ans=[]
    while D>2:
        ans.append(1)
        S-=1
        D-=1
    if D==2:
        if S>9:
            ans.append(S-9)
            ans.append(9)
        else:
            ans.append(1)
            ans.append(S-1)
    carry=0
    for i in range(-1,-len(ans)-1,-1):
        if ans[i]>9:
            carry=ans[i]%9
            ans[i]=9
            ans[i-1]=ans[i-1]+carry
    ans[-1]+=1
    ans[-2]+=1
    carry=0
    for i in range(-1,-len(ans)-1,-1):
        if ans[i]>9:
            carry=ans[i]%9
            ans[i]=9
            ans[i-1]+=carry
    return str("".join(ans))

print(secondSmallest(16,3))
