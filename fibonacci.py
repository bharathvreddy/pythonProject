# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(5))


'''def sum(n):
    assert n<=10
    if n%2==0:
        print(n)
        return sum(n+2)
    else:
        return sum(n+1)
print(sum(1))'''


'''def func(s):
    biggestnum=s[0]
    for i in range (1,len(s)):
        if s[i]>biggestnum:
            biggestnum=s[i]
    print(biggestnum)


func([2,3,55,6,86])




def f(samplearray,n):
    if n==1:
        return samplearray[0]
    return max(samplearray[n-1],f(samplearray,n-1))


print(f([1,2,3,4,5],5))'''

# a=[1,2,3,4,5,6,67,8]
# a[-1]=10
# print(a)
A="11101110011"
# print(len(A[4]))
#permutations
# def o(arr,ds,freq,ans):
#     if len(arr)==len(ds):
#         ans.append(ds.copy())
#         return
#
#     for i in range(len(arr)):
#         if freq.get(i,False)==False:
#             ds.append(arr[i])
#             freq[i]=True
#             o(arr,ds,freq,ans)
#             ds.pop()
#             freq[i]=False
#     return ans
# # print(o([1,2,3],[],{},[]))
# a=[[1,10],[2,2]]
# a.sort(key=lambda x:x[1])
# print(a)
# n=int(input("Enter no. of queens"))
# col=set()
# posdiag=set()
# negdiag=set()
# board=[["0"]*n for i in range(n)]
# ans=[]
# def backtrack(r):
#     if r==n:
#         copy=["".join(row) for row in board]
#         ans.append(copy)
#         return
#     for c in range(n):
#         if c in col or r+c in posdiag or r-c in negdiag:
#             continue
#         col.add(c)
#         posdiag.add(r+c)
#         negdiag.add(r-c)
#         board[r][c]="Q"
#         backtrack(r+1)
#         col.remove(c)
#         posdiag.remove(r+c)
#         negdiag.remove(r-c)
#         board[r][c]="0"
# # backtrack(0)
# print(ans)
# a=[1,2,3,4,5,6,7,8,9,0]
# from functools import reduce
# q=reduce(lambda x,y:x+y,a)
# print(q)
#merging two sorted arrays
# def solve(A, B):
#     c = []
#     i = 0
#     j = 0
#     while i < len(A) and j < len(B):
#         if A[i] < B[j]:
#             c.append(A[i])
#             i+=1
#         else:
#             c.append(B[j])
#             j+=1
#
#     if i == len(A):
#         c += B[j:]
#     else:
#         c += A[i:]
#     return c
# print(solve([1],[4]))
# # a=[5,3,7,12,8]
# for i in range(9):
#     index=i
#     min_so_far=a[i]
#     for j in range(i+1,len(a)):
#         if min_so_far>a[j]:
#             min_so_far=a[j]
#             index=j
#     a[i],a[index]=a[index],a[i]
# print(a)
# a=[1,2]
# a.sort()
# initial=a[0]
# for i in range(1,len(a)):
#     if a[i]!=initial+1:
#
#         print(0)
#         break
#     else:
#         initial = a[i]
# else:
#     print(1)
# max1=max(a)
# second_max=a[0]
# for i in range(1,len(a)):
#     if a[i]>second_max and a[i]<max1:
#         second_max=a[i]
# print(max1,second_max)
# def vest(n):
# #     if n<10:
# #         return n
# #     else:
# #         return n%10+vest(n//10)
# # print(vest(4650))
# max1=a[0]
# max2=a[0]
# for i in range(1,len(a)):
#     if a[i]>max1:
#         max1=a[i]
# print(max1,max2)
# def vest(n):
#     if n<10 :
#         if n==1:
#             return 1
#         else:
#             return 0
# a=["900","7"]
# a.sort(key=lambda x:x[0],reverse=1)
# print(a)
# from functools import cmp_to_key
# for i in range(1,9):
#     print(i)

# def f(index,previndex):
    # if dp[index][previndex]!=None:
    #     return dp[index][previndex]
    # if index==-1:return 0
    # notpick=0+f(index-1,previndex)
    # pick=float("-inf")
    # if previndex==len(array):
    #     pick=array[index]+f(index-1,index)
    # if previndex!=len(array) and array[index]<array[previndex] and index+1!=previndex:
    #     pick = array[index] + f(index - 1, index)
    # dp[index][previndex]=max(pick,notpick)
    # return dp[index][previndex]
#     for index in range(len(array)):
#         for previndex in range(len(array)+1):
#             notpick=dp[index-1][previndex]
#             pick=float("-inf")
#             if previndex==len(array):
#                 pick=array[index]+dp[index-1][index]
#             if previndex!=len(array) and array[index]<array[previndex] and index+1!=previndex:
#                 pick = array[index] + dp[index - 1][index]
#             dp[index+1][previndex]=max(pick,notpick)
#     return dp[-1][-1]
# array=[1,74,56,29,108]
# dp=[[0 for i in range(len(array)+1)] for j in range(len(array)+1)]
# print(f(len(array)-1,len(array)))
# print(dp)
# from collections import defaultdict
# class Solution:
#     def makeConnected(self, n,connections):
#         if len(connections) >= n - 1:
#             pass
#         else:
#             return -1
#         dict = defaultdict(list)
#         for src, dst in connections:
#             dict[src].append(dst)
#             dict[dst].append(src)
#         # print(dict)
#         visited = [False for i in range(n)]
#
#         self.bfs(visited, dict)
#         # print(visited)
#         count = 0
#         for i in visited:
#             if i == False:
#                 count += 1
#         return count
#
#     def bfs(self, visited, dict):
#         queue = []
#         queue.append(0)
#         visited[0] = True
#         while len(queue) > 0:
#             q = queue.pop()
#             for ele in dict[q]:
#                 if visited[ele] == False:
#                     visited[ele] = True
#                     queue.append(q)

def minPathSum(grid):
    grid1 = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            d, e = float("inf"),float("inf")
            if i - 1 >= 0:
                d =grid1[i - 1][j]
            if j - 1 >= 0:
                e = grid1[i][j - 1]
            minn=min(d,e)
            if minn==float("inf"):
                minn=0
            grid1[i][j] = grid[i][j]+minn

    print(grid1)
minPathSum([[1,3,1],[1,5,1],[4,2,1]])

