# class Test:
#     def __init__(self,x,c):
#         self.name=x
#         self.age=c
#
#     def prin(self):
#         return self.age,self.name
#
#
# t1=Test("Bharath",20)
# t2=Test("Bharath",20)
#
#
# print(t1.prin()==t2.prin)

# from itertools import combinations_with_replacement
# cse=[]
# raj=[]
# n=input().split(" ")
# a=list([int(x) for x in n])
# y=combinations_with_replacement(a,2)
# for n1 in y:
#     cse.append(n1)
#
# for (l,m) in cse:
#     raj.append(l**2+m**2)
#
# for mkm in raj:
#     if raj.count(mkm)>1:
#         print(mkm)
#         break

# a=[16,54,19,354,5432]
# for i in a:
#     if i%5==0:
#         print("undhi")
#         break
# print("asdf")


# lst=[1,2,34]
# print(lst.index(2))
#
#
# class Treenode:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]
#
#     def addchild(self,obj,x):
#         obj.children.append(x)
#
#
# Drinks=Treenode("Drinks")
# Hot=Treenode("Hot")
# Cold=Treenode("Cold")
# Drinks.addchild(Drinks,Hot)
# Drinks.addchild(Drinks,Cold)
#
# print(Drinks.children[0].data)


# a = "1010"
# b = "1011"
# a=int(a,2)+int(b,2)
# print(bin(a)[2:])

# def raj(a):
#     if len(a)==0:
#         return ""
#     else:
#         return a[-1] + raj(a[:-1])
# print(raj("hello"))
#should return empty string ""

# def reverse(s):
#     if len(s)==0:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
# print(reverse("hello"))

# def  raj(a):
#     if len(a)==1 or len(a)==0:
#         return True
#     if a[0]==a[-1]:
#         return raj(a[1:-1])
#     else:
#         return False
# print(raj("kajlak"))

# def dec(a):
#     if a==1:
#         return "1"
#     else:
#         return dec(a//2)+str(a%2)
# print(dec(3))

# def rec(n):
#     if n==1:
#         return 1
#     else:
#         return n + rec(n-1)
#
# print(rec(10))
# import math
# name=input()
# fact=math.factorial(int(name))
# list1=list(str(fact))
# n=len(list1)
# list1.reverse()
# for i in range(len(list1)):
#     if list1[i]!="0":
#         print(int(list1[i]))
#         break
#
# num=input("string")
# k=int(input("size"))
# l=len(num)
# i=0
# max1=[]
# while k<=len(num):
#     max1.append(int(num[i:k]))
#     i+=1
#     k+=1
# print(max(max1))
# def com(arr,index,target,sum,subarr,ans):
#     if index<len(arr):
#         if sum==target:
#             ans.copy(subarray)
#             return
#     if sum>target:
#         return
#     com(arr,index+1,target,sum+arr[index],subarr+[arr[index]],ans)
#     com(arr,index+1,target,sum,subarr,ans)
# com([1,2,3],0,6,0,[],[])
# def jump(array,index): #memorization
#     def raj(array,index,dict):
#         if index==0:
#             return 0
#         if index in dict:
#             return dict[index]
#         left=raj(array,index-1,dict)+abs(array[index]-array[index-1])
#         if index==1:
#             return float("inf")
#         right=raj(array,index-2,dict)+abs(array[index]-array[index-2])
#         dict[index]=min(left,right)
#         return min(left,right)
#     return raj(array,index,{})
# print(jump([10 ,20 ,30 ,10],3))
# def ballgame():
#     friends=10
#     array=[i for i in range(1,friends+1)]
#     time=18
#     eo=time//(friends-1)
#     rema=time%(friends-1)
#     if rema==0 and eo%2!=0:
#         return array[-2],array[-1]
#     if rema==0 and eo%2==0:
#         return array[1],array[0]
#     if eo%2==0:
#         return array[rema-1],array[rema]
#     else:
#         return array[-rema],array[-rema-1]
# print(ballgame())

#coin problem squares
# dp={0:0,1:1,2:2,3:3}
# def f(n):
#     sum1=float("inf")
#     if n in dp:
#         return dp[n]
#     for i in range(1,5): #or (5,0,-1)
#         if i*i>n:
#             break          #continue
#         dp[n]=min(dp.get(n,float("inf")),1+f(n-(i*i)))
#     return dp[n]
# # print(f(15))
#
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("class A")
#
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("class B")

# A1=A()
# B1=B()
# A1.run()
# B1.run()
# A=[[-1]*3]*3
# A[0][0]=12
# print(id(A[0]))
#binary search
# a=[1,2,3,4,6,6,6,8,9,10,11]
# target=6
# s=0
# e=len(a)-1
# ans=-1
# while s<=e:
#     mid=(s+e)//2
#     if a[mid]==target:
#         ans=mid
#         e=mid-1 #for finding last instance s=mid+1
#         continue
#         # print(mid)
#         # break
#     if a[mid]<target:
#         s=mid+1
#     else:
#         e=mid-1
# print(ans)

#lower bound-first element greater than or equal to target
# def lowerbound(a,target):
#     s=0
    # e=len(a)-1
    # ans=e
    # while (s<=e):
    #     mid=(s+e)//2
    #     if a[mid]>=target:
    #         ans=mid
    #         e=mid-1
    #     else:
    #         s=mid+1
    # return a[ans]
# print(lowerbound([1,2,3,4,7,8],5))


#upper bound
# def upperbound(a,target):
#     s=0
#     e=len(a)-1
#     ans=e
#     while (s<=e):
#         mid=(s+e)//2
#         if a[mid]>target:
#             ans=mid
#             e=mid-1
#         else:
#             s=mid+1
#     return a[ans]
# print(upperbound([1,2,3,4,5,7,8],6))

# ans=[]
# T=int(input())
# for i in range(T):
#     n,m=map(int,input().split())
#     ans=[list(map(int,input().split())) for k in range(n)]
#     print(ans)
#     ans1=float("inf")
#     kavali=0
#     kr=[]
#     def f(i,j,total,ds):
#         global ans1,kavali,kr
#         if i==0 and j==0:
#             total+=ans[0][0]
#             ds.append(ans[0][0])
#             if total<ans1:
#                 ans1=total
#                 kavali=max(ds)
#                 kr=ds[:]
#             return
#         if i<0 or j<0:
#             return float("-inf")
#         left=f(i,j-1,total+ans[i][j],ds+[ans[i][j]])
#         up=f(i-1,j,total+ans[i][j],ds+[ans[i][j]])
#         return kavali,kr
    # print(f(n-1,m-1,0,[]))
#
# def f(num):
#     s=int(str(abs(num))[::-1])
#     print(s)
# f(-34834465735)

# dp=[[0]*(5+1) for i in range(3+1)]
# print(dp)
# def f(index,target,ds,k):
#     if dp[index][target]!=0:
#         return dp[index][target]
#     if target==0:
#         k.append(ds.copy())
#         return
#
#     if index==0:
#         if target==array[0]:
#             ds.append(array[0]) #such a fool you are.....
#             k.append(ds.copy())
#         return
#
#     notpick=f(index-1,target,ds,k)
#     pick=0
#     if array[index]<=target:
#         pick=f(index-1,target-array[index],ds+[array[index]],k)
#     return k
# array=[4,3,2,1]
# print(f(3,5,[],[]))

# dp=[[0]*(5+1) for i in range(3+1)]
# print(dp)
# target=5
# for i in dp:
#     i[0]=1
# for i in range(target):
#     if i==array[0]:
#         dp[0][i]=1
#         break
# print(dp)
# for index in range(1,len(dp)):
#     for target in range(1,len(dp[0])):
#         notpick = dp[index - 1][target]
#         pick = 0
#         if array[index] <= target:
#             pick = dp[index - 1][target - array[index]]
#         dp[index][target]=pick+notpick
#
# print(dp)
# a=[1]
# print(a)
# b=list([1])
# print(id(b))
#binary tree
# class Tree:
#     def __init__(self,val):
#         self.value=val
#         self.left=None
#         self.right=None
#
# def addleftnode(parent,kid):
#     parent.left=kid
#
# def addrightnode(parent,kid):
#     parent.right=kid
#
# def display(rootnode):
#     if not rootnode:
#         return
#     if rootnode.left:
#         print(rootnode.value,"is parent of ",rootnode.left.value)
#         display(rootnode.left)
#     if rootnode.right:
#         print(rootnode.value," is parent of ",rootnode.right.value)
#         display(rootnode.right)
# def height(rootnode):
#     if not rootnode:
#         return 0
#     left=1+height(rootnode.left)
#     right=1+height(rootnode.right)
#     return max(left,right)
#
# def levelordertraversal(rootnode):
#     if not rootnode:
#         return
#     stack=[]
#     stack.append(rootnode)
#     while len(stack)!=0:
#         a=stack.pop(0)
#         print(a.value)
#         if a.left:
#             stack.append(a.left)
#         if a.right:
#             stack.append(a.right)
# flag=0
# def isbalanced(root):
#     global flag
#     if not root:
#         return True
#     l=1+isbalanced(root.left)
#     r=1+isbalanced(root.right)
#     if abs(l-r)>1:
#         flag=1
#     return max(l,r)
# if flag==1:
#     print("False....")
# else:
#     print("True")

# a=Tree(50)
# b=Tree(40)
# addleftnode(a,b)
# c=Tree(20)
# addrightnode(a,c)
# d=Tree(10)
# e=Tree(5)
# f=Tree(1)
# addleftnode(c,d)
# addrightnode(c,e)
# addleftnode(e,f)
# # display(a)
# # print(height(a))
# # levelordertraversal(a)
# stack=[]
# def level(root):
#     if not root:
#         return
#     stack.append(root)
#     if root.left:
#         level(root.left)
#     if root.right:
#         level(root.right)

# q=[]
# def height(rootnode):
#     if not rootnode:
#         return 0
#     left=1+height(rootnode.left)
#     right=1+height(rootnode.right)
#     g=max(left,right)
#     # q.append(g)
#     return g
#
# def isBalanced(root):
#     l1=height(root.left)+1
#     r1=height(root.right)+1
#     if abs(l1-r1)>1:
#         return False
#     return True
#
# def check():
#     ans=True
#     for i in stack:
#         ans=ans*isBalanced(i)
#     return ans
# level(a)
# print(check())
# print(q)
# ans=True
# def add(root):
#     global ans
#     if not root:
#         return True
#     l=1+add(root.left)
#     r=1+add(root.right)
#     if abs(l-r)>1:
#         ans=False
#     return max(l,r)
# add(a)
# print(ans)
# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.Right=None
#
# a=Node(1)
# b=Node(2)
# c=Node(3)
# d=Node(4)
# a.left=b
# b.left=c
# a.right=d
# def k(root,list):
#     if root is None:
#         return
#     if root.left is None and root.right is None:
#         print(sum(list)+root.val)
#         return
#     k(root.left,list+[root.val])
#     k(root.right,list+[root.val])
# k(a,[])

# arr=[0,-2,0,-1,4]
# cul=[0 for i in range(len(arr))]
# prev=""
# prev1=-1
# for i,e in enumerate(arr):
#     if prev=="":
#         if e>0:
#             cul[i]=1
#             prev="p"
#         elif e<0:
#             cul[i]=-1
#             prev="n"
#         else:
#             cul[i]="N"
#             prev=""
#     elif prev=="p" :
#         if e<0:
#             cul[i]=-1
#             prev="n"
#         if e>0:
#             cul[i]=1
#             prev="p"
#         if e==0:
#             cul[i]="N"
#             prev=""
#     else:
#         if e<0:
#             cul[i]=1
#             prev="n"
#         elif e>0:
#             cul[i]=-1
#             prev="p"
#         else:
#             cul[i]="N"
#             prev=""
# print(cul)
# ans=0
# first_one=float("inf")
# first_neg=float("inf")
# for i,e in enumerate(cul):
#     if e=="N":
#         first_one = float("inf")
#         first_neg = float("inf")
#     elif e==1:
#         if first_one==float("inf"):
#             first_one=i
#         ans=max(ans,i-first_one+1)
#     else:
#         if first_neg==float("inf"):
#             first_neg=i
#         ans=max(ans,i-first_neg+1)
# print(ans)
#good stones gfg
# def f(arr):
#     good,bad=0,0
#     bad_path=list()
#     good_path=list()
#     for i in range(len(arr)):
#         cur_pos=i
#         this_path=list()
#         while cur_pos>-1 and cur_pos<len(arr) and cur_pos not in this_path and cur_pos not in bad_path and cur_pos not in good_path:
#             this_path.append(cur_pos)
#             cur_pos=cur_pos+arr[cur_pos]
#             if cur_pos in good_path or cur_pos<0 or cur_pos>len(arr)-1:
#                 good_path.extend(this_path)
#                 good+=len(this_path)
#                 continue
#             if cur_pos in this_path or cur_pos in bad_path:
#                 bad+=len(this_path)
#                 bad_path.extend(this_path)
#                 continue
#     return len(good_path)
# print(f([2,3,-1,2,-2,4,1]))

# class Solution:
    #-1 not visited
    # 0 bad stone
    # 1 Good stone
#     def dfs(self, ind, arr, dp):
#         if ind < 0 or ind >= len(arr):
#             return 1
#         if dp[ind] != -1:
#             return dp[ind]
#         dp[ind]=0
#         dp[ind] = self.dfs(ind + arr[ind], arr, dp)
#         return dp[ind]
#
#     def goodStones(self, n, arr):
#         dp = [-1 for i in range(n)]
#         for i in range(n):
#             self.dfs(i, arr, dp)
#         count=0
#         for i in dp:
#             if i:
#                 count+=1
#         return count
#
# a=Solution()
# print(a.goodStones(7,[-4,-1,-3,4,1,-3,-4]))

# def f(a,m):
#     ans=-1
#     left=right=0
#     while right<len(a):
#         if a[right]=="a":
#             right+=1
#
#         else:
#             if m>0:
#                 # right+=1
#                 m-=1
#
#             else:
#                 while a[left]=="a":
#                     left+=1
#                 left+=1
#             ans=max(ans,right-left+1)
#             right+=1
#
#     return ans
# print(f("oaaoaoaoaoaoooaoao",3))
#leetcode 35
# print(3^3^1)

# def f(capital,profits,k,index,capital_amount):
#     if k==0 or index>=len(profits):
#         return 0
#     take=float("-inf")
#     if capital[index]<=capital_amount:
#         take=profits[index]+f(capital,profits,k-1,index+1,capital_amount-capital[index]+profits[index])
#     not_take=0+f(capital,profits,k,index+1,capital_amount)
#     return max(take,not_take)
# print(f(k =1,capital_amount =2,profits =[1,2,3],capital =[1,1,2],index=0))

#gfg 23 feb
# def uniquepaths(grid):
#     if grid[0][0]==0 or grid[-1][-1]==0:return 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if i==j==0:
#                 continue
#             up,left=0,0
#             if grid[i][j]==1:
#                 if i-1>=0:
#                     up=grid[i-1][j]
#                 else:
#                     up=0
#                 if j-1>=0:
#                     left=grid[i][j-1]
#                 else:
#                     left=0
#                 grid[i][j]=left+up
#     print(grid)
# grid=[[1,0,1]]
# uniquepaths(grid)

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         # cache=defaultdict(bool)
#
#         def dfs(i,j):
#             # list1 = ["*", "?,", "."]
#             # if i==0 and j==0:
#             #     if s[i]!=p[j]:
#             #         return False
#             if i<0 and j<0:
#                 return True
#             if i<0:
#                 if j>=0:
#                     for ele in range(0,j+1):
#                         if p[ele]!="*":
#                             return False
#                     return True
#             if j<0:
#                 if i>=0:
#                     return False
#
#
#             if s[i]==p[j]:
#                 return dfs(i-1,j-1)
#
#             if p[j]==".":
#                 return dfs(i-1,j-1)
#             if p[j]=="*":
#                 leave=dfs(i,j-1)
#                 pick=dfs(i-1,j)
#                 return pick or leave
#             return False
#
#
#         return dfs(len(s)-1,len(p)-1)
# k=Solution()
# print(k.isMatch("abcdefgho","**"))
#potd gfg
# def secondSmallest( S, D):
#     if S >=D * 9:
#         return -1
#     ans = [0 for i in range(D)]
#     ans[0] = 1
#     S -= 1
#     D -= 1
#     ind = len(ans) - 1
#     for i in range(len(ans) - 1, -1, -1):
#         if S >= 9:
#             ans[i]+= 9
#             S -= 9
#             ind = i
#         else:
#             ans[i]+= S
#             S = 0
#     print(ans)
#     ans[ind] = ans[ind] - 1
#     ans[ind - 1] = ans[ind - 1] + 1
#     return int("".join(map(str, ans)))
# print(secondSmallest(26,3))

# class node:
#     def __init__(self,value):
#         self.val=value
#         self.left=None
#         self.right=None
# Node9=node(9)
# Node4=node(4)
# Node0=node(0)
# Node5=node(5)
# Node1=node(1)
# Node4.left=Node9
# Node4.right=Node0
# Node9.left=Node5
# Node9.right=Node1
#
# class Solution:
#     ans=0
#     def sumNumbers(self, root):
#         def dfs(root,value):
#             if root.left is None and root.right is None:
#                 value=value+str(root.val)
#                 Solution.ans+=int(value)
#                 return
#             if root.left is not None:
#                 dfs(root.left,value+str(root.val))
#             if root.right is not None:
#                 dfs(root.right,value+str(root.val))
#         dfs(root,"")
#         return Solution.ans
#
# k=Solution()
# print(k.sumNumbers(Node4))

# def uniquePathsWithObstacles(obstacleGrid):
#     grid = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
#     if obstacleGrid[0][0] == 1:
#         return 0
#
#     for i in range(len(obstacleGrid)):
#         for j in range(len(obstacleGrid[0])):
#             if i==0 and j==0:
#                 grid[0][0]=1
#             else:
#                 if obstacleGrid[i][j]==0:
#                     k,ele=0,0
#                     if i-1>=0:
#                         k=grid[i-1][j]
#                     if j-1>=0:
#                         ele=grid[i][j-1]
#                     grid[i][j]=k+ele
#                 else:
#                     grid[i][j]=0
#     return grid[-1][-1]
# print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
from collections import defaultdict
class Solution:
    def minScore(self,n,roads):
        dict = defaultdict(list)
        for i, j, wei in roads:
            dict[i].append((j, wei))
            dict[j].append((i, wei))
        visited = [False for i in range(n+1)]
        self.bfs(1, visited, dict)
        ans = float("inf")
        for node in range(len(visited)):
            if visited[node]:
                for k, w in dict[node]:
                    ans = min(ans, w)
        return ans

    def bfs(self, node, visited, dict):
        queue = [node]
        visited[node] = True
        ans=float("inf")
        while len(queue) > 0:
            q = queue.pop()
            for e, w in dict[q]:
                if visited[e]==False:
                    queue.append(e)
                    visited[e] = True
                ans=min(ans,w)
        return ans

obj=Solution()
print(obj.minScore(4,[[1,2,2],[1,3,4],[3,4,7]]))