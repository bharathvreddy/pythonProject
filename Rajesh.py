# import time,random
# g=time.time()
# class Solution:
#     res=0
#     def countWaystoDivide(self, n, k):
#         Solution.res=0
#         return self.charge(0,0,0,n,k)
#     def charge(self,prev_ele,sum,ele_len,n,k):
#         global res
#         if sum>n or ele_len>k:
#             return
#         if sum==n and ele_len==k:
#             Solution.res+=1
#             return
#         for ele in range(1,n+1):
#             if ele>=prev_ele:
#                 self.charge(ele,sum+ele,ele_len+1,n,k)
#         return Solution.res
#
# print(random.randint(1,78))
# k=Solution()
# print(k.countWaystoDivide(115,4))

# class Solution:
#     def minPathSum(self, grid):
#         grid1 = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if i == 0 and j == 0:
#                     grid1[0][0] = grid[0][0]
#                 else:
#                     up = grid[i][j]
#                     if i - 1 >= 0:
#                         up += grid1[i - 1][j]
#                     else:
#                         up = float("inf")
#
#                     left=grid[i][j]
#                     if j - 1 >= 0:
#                         left += grid1[i][j - 1]
#                     else:
#                         left=float("inf")
#                     grid1[i][j] = min(up, left)
#         return grid1
#
# k=Solution()
# print(k.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

# def sum(grid):
#     grid[1]=max(grid[0],grid[1])
#     for i in range(2,len(grid)):
#         grid[i]=max(grid[i]+grid[i-2],grid[i-1])
#     print(grid)
# sum([5, 1,0, 10, 10, 500])

# import time
# g=time.time()
# for i in range(10000000):
#     # print("k")
#     pass
# print(time.time()-g)

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#
# def maximumNonAdjacentSum(nums):
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return max(nums)
#     nums[1]=max(nums[0],nums[1])
#     for ele in range(2, len(nums)):
#         take = nums[ele] + nums[ele - 2]
#         # if ele-2>=0:
#         #     take+=nums[ele-2]
#         not_take = nums[ele - 1]
#
#         nums[ele] = max(not_take, take)
#     return nums[-1]
# print(maximumNonAdjacentSum(([84 ,83, 7, 82, 97, 67, 74, 87, 57, 16])))

# Main.
# t = int(stdin.readline().rstrip())
#
# while t > 0:
#     n = int(stdin.readline().rstrip())
#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     print(maximumNonAdjacentSum(arr))

# def maxIntersections(lines, N):
#     lines.sort(key=lambda x:x[1])
#     print(lines)
#     cur_end=lines[0][1]
#     score=1
#     res=0
#     for index in range(1,N):
#         s,e=lines[index][0],lines[index][1]
#         if s<=cur_end:
#             score+=1
#             res=max(res,score)
#         else:
#             cur_end=e
#             score=1
#     print(res)
# maxIntersections([[-4,7],[-4,2],[4,9],[-2,10],[7,9],[-2,7]],6)

# def minimumPathSum(dp, n):
#     for i in range(1,n):
#         dp[i][0]+=dp[i-1][0]
#     for i in range(1,n):
#         for j in range(1,i+1):
#             ab=float("inf")
#             if j<i:
#                 ab=dp[i-1][j]
#             dp[i][j]+=min(ab,dp[i-1][j-1])
#     print(min(dp[-1]))
#
#
#
# # minimumPathSum([[1],[2,3],[3,6,7],[8,9,6,12]],4)
#
# def getMaxPathSum(dp):
#     for i in range(1,len(dp)):
#         for j in range(len(dp[0])):
#             a=float("inf")
#             if j-1>=0:
#                 a=dp[i-1][j-1]
#             b=float("inf")
#             if j+1<=len(dp[0])-1:
#                 b=dp[i-1][j+1]
#             dp[i][j]+=min(a,b,dp[i-1][j])
#     return dp
# print(getMaxPathSum([[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]))

# def count(arr, n):
#     target=7
#     dp=[[0 for i in range(target+1)] for j in range(n)]
#     for i in dp:
#         i[0]=1
#     if arr[0]<=target:
#         dp[0][arr[0]]=1
#     for index in range(1,len(dp)):
#         for target in range(1,len(dp[0])):
#             pick=0
#             if target>=arr[index]:
#                 pick=dp[index-1][target-arr[index]]
#             not_pick=dp[index-1][target]
#             dp[index][target]=pick + not_pick
#     return dp[-1][-1]
# print(count([1,3,3,4],4))


# class Solution:
#     def coin(self,coins,amount,index):
#         if index==0:
#             if amount%coins[0]==0:
#                 return amount//coins[0]
#             else:
#                 return float("inf")
#         pick=float("inf")
#         if amount>=coins[index]:
#             pick=1+self.coin(coins,amount-coins[index],index)
#         not_pick=self.coin(coins,amount,index-1)
#         return min(pick,not_pick)
#
#     def coinChange(self, coins, amount):
#         index=len(coins)-1
#         return self.coin(coins,amount,index)
# k=Solution()
# print(k.coinChange([1,2,5],11))
# def f(root):
#     if root.left is None and root.right is None:
#         return
#     if not root.left :return
#     if not root.right:return
#     f(root.left)
#     f(root.right)
#     a,b,c,d=0,0,0,0
#     if root.right.right:
#         a=root.right.right.val
#     if root.right.left:
#         b=root.right.left.val
#     if root.left.left:
#         c=root.left.left.val
#     if root.left.right:
#         d=root.left.right.val
#     root.val=max(root.val+max(a,b,c,d),max(root.right,root.left))
#     return root.val
#
#
# class node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
# A=node(10)
# B=node(1)
# C=node(4)
# D=node(1)
# E=node(200)
# F=node(133)
# G=node(6)
# H=node(4)
# A.left=B
# B.left=C
# B.right=D
# C.left=E
# C.right=F
# D.left=G
# D.right=H
# print(f(A))
#Printing subsequences
# def func(dp,str1,str2):
#     i=len(dp)-1
#     j=len(dp[0])-1
#     str=""
#     while (i>=0 and j>=0):
#         if str1[i]==str2[j]:
#             str+=str1[i]
#             i-=1
#             j-=1
#         else:
#             if dp[i-1][j]>dp[i][j-1]:
#                 i-=1
#             else:
#                 j-=1
#     if i:
#         if str1[i-1]==str2[j]:
#             str+=str2[j]
#     else:
#         if str2[j-1]==str1[i]:
#             str+=str1[i]
#     return str[::-1]
#
# #length of common subsequences
# def longestCommonSubsequence(text1: str, text2: str) -> int:
#     dp=[[0 for i in range(len(text1))]for j in range(len(text2))]
#     k = 0
#     for i in range(len(text2)):
#         if text2[i] == text1[0]:
#             k = 1
#             dp[0][i] = k
#         else:
#             dp[0][i]=k
#     k = 0
#     for i in range(len(text1)):
#         if text1[i] == text2[0]:
#             k = 1
#             dp[i][0] = k
#         else:
#             dp[i][0]=k
#     for i in range(1, len(dp)):
#         for j in range(1, len(dp[0])):
#             if text1[i] == text2[j]:
#                 dp[i][j] = 1 + dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#     for i in dp:
#         print(i)
#     k=func(dp, text1, text2)
#     return k
# print(longestCommonSubsequence("aaaabbaa",'aabbaaaa'))

# def primeSubOperation(nums) -> bool:
#     primes = [True for i in range(1001)]
#     primes[0]=False
#     for i in range(2, 1000):
#         for j in range(2, 1000):
#             if i * j <= 1000:
#                 primes[i * j] = False
#     print(primes)
#     for i in range(len(nums)-2,-1,-1):
#         if nums[i]>=nums[i+1]:
#             for prime in range(1,nums[i]):
#                 if primes[prime]==1 and nums[i]-prime<nums[i+1]:
#                     nums[i]-=prime
#                     break
#     return nums
#     # print(nums[i],nums[i+1])


n=5
arr=[1,2]
ans=[]
# def backtrack(length,temp):
#     if length==n:
#         ans.append(temp.copy())
#         return
#     for i in arr:
#         temp.append(i)
#         backtrack(length+1,temp)
#         temp.pop()
# backtrack(0,[])
# print(len(ans),ans)

# import heapq
# def maxSlidingWindow(nums,k):
#     if k == 1:
#         return nums
#     left = 0
#     li = []
#     res = []
#     for i in range(k-1,len(nums)):
#         if len(li)==0:
#             for ele in range(k):
#                 heapq.heappush(li,-nums[ele])
#             res.append(-li[0])
#         else:
#             li.remove(-nums[left])
#             left+=1
#             heapq.heappush(li,-nums[i])
#             res.append(-li[0])
#         print(li)
#     return res
# print(maxSlidingWindow([1,3,1,2,0,5],3))


# def sumPrime(rangeLeft,rangeRight):
#     def isprime(number):
#         for i in range(2,number):
#             if number%i==0:
#                 return False
#         return True
#
#     for i in range(rangeLeft,rangeRight+1):
#         count=0
#         if isprime(i):
#             count+=i
#     return count

