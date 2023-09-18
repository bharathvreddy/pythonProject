# # Stack using linked list
# #SUCCESSFULLY DONE
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class head:
#     def  __init__(self):
#         self.head=None
#
#     def push(self,value):
#         b=Node(value)
#         if self.head==None:
#             self.head=b
#             # print(self.head.data)
#         else:
#             b.next=self.head
#             self.head=b
#              # print(self.head.data)
#
#     def pop(self):
#         self.head=self.head.next
#
#     def display(self):
#         temp=self.head
#         while temp!=None:
#             print(temp.data)
#             temp=temp.next
#
#     def peek(self):
#         print(self.head.data)
#
#     def delete(self):
#         self.head=None


# ant=head()
# ant.push(1)
# ant.push(2)
# ant.push(3)
# ant.display()
# # ant.pop()
# # print()
# # ant.display()
# # print()
# # ant.peek()
#
#
#
# from collections import deque
# custom=deque()
# print(custom)
# custom.append(1)
# custom.append(2)
# custom.append(3)
# print(custom.__contains__(5))
# print()
# print(custom.__len__())
# print(custom)
# custom.append(4)
# print(custom)
# print()
#
# print("2nd")
# # print( )
# import queue as q
# customq=q.Queue(maxsize=3)
# # customq.put(2)
# # customq.put(3)
# # customq.put(4)
# # a=customq.get()
# # print(a)
# # print(customq.queue)
# #
# #
# #
# # print()
# # print("LEVEL ORDER TRAVERSAL:")
# # print()
#
# # class run:
# #    def add(self):
# #        return "adding"
#
# # a=run()
# # a=None
# # print(a is None)
#
# # import Tree
# # print(__name__)
#
# import queue
# #BINARY SEARCH TREE
# class BST:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def insert1(rootnode,value):
#     if rootnode.data is None:
#         rootnode.data=value
#     elif value<=rootnode.data:
#         if rootnode.left is None:
#             rootnode.left=BST(value)
#         else:
#             insert1(rootnode.left,value)
#     else:
#         if rootnode.right is None:
#             rootnode.right=BST(value)
#         else:
#             insert1(rootnode.right,value)
# def Levelordertraversal(rootnode):
#     if rootnode.data is None:
#         return "Nothing to print"
#     else:
#         q=queue.Queue()
#         q.put(rootnode)
#         while not(q.empty()):
#             a=q.get()
#             print(a.data)
#             if a.left is not None:
#                 q.put(a.left)
#             if a.right is not None:
#                 q.put(a.right)
#
# def Preordertraversal(rootnode):
#     if rootnode is None:
#         return
#     else:
#         print(rootnode.data)
#         Preordertraversal(rootnode.left)
#         Preordertraversal(rootnode.right)
#
# def Inordertraversal(rootnode):
#     if rootnode is None:
#         return
#     else:
#
#         Inordertraversal(rootnode.left)
#         print(rootnode.data)
#         Inordertraversal(rootnode.right)
#
# def Postordertraversal(rootnode):
#     if rootnode is None:
#         return
#     else:
#
#         Postordertraversal(rootnode.left)
#
#         Postordertraversal(rootnode.right)
#
#         print(rootnode.data)
# def search(rootnode,value_to_search):
#     if rootnode.data is None:
#         return "Nothing to print"
#     else:
#         q=queue.Queue()
#         q.put(rootnode)
#         while not(q.empty()):
#             a=q.get()
#             if a.data==value_to_search:
#                 print("value found")
#                 break
#             if a.left is not None:
#                 q.put(a.left)
#             if a.right is not None:
#                 q.put(a.right)
#         else:
#             print("Value not found")
# def minvalue(rootnode):
#     while rootnode is not None:
#         current =rootnode.left
#     return current
#
#
# def deleteNode(rootnode,nodevalue):
#     if rootnode is None:
#         return rootnode
#     elif nodevalue<rootnode.data:
#         rootnode.left=deleteNode(rootnode.left,nodevalue)
#         print( rootnode.left.data)
#     elif nodevalue>rootnode.data:
#         rootnode.right=deleteNode(rootnode.right,nodevalue)
#     else:
#         if rootnode.left is None:
#             temp=rootnode.right
#             rootnode=None
#             return temp
#         if rootnode.right is None:
#             temp=rootnode.left
#             rootnode=None
#             return temp
#         temp=minvalue(rootnode.right)
#         rootnode.data=temp.data
#         rootnode.right=deleteNode(rootnode.right,temp.data)
#     return rootnode
#
#
#
#
# a=BST(100)
# insert1(a,90)
# insert1(a,85)
# insert1(a,110)
# insert1(a,80)
# insert1(a,120)
# # display(a)
# # search(a,90)
#
# deleteNode(a,80)
# Levelordertraversal(a)
#
#

# a=list(map(int,input().split()))
# rot=int(input())
# b=a.pop(0)
# if rot>len(a):
#     rot=rot%len(a)
# a.reverse()
# print("a is ",a)
#
# i=0
# j=rot-1
# while(i<j):
#     a[i],a[j]=a[j],a[i]
#     i+=1
#     j-=1
# l=rot
# m=len(a)-1
# while(l<m):
#     a[l],a[m]=a[m],a[l]
#     l+=1
#     m-=1
# for s in a:
#     print(s,end=" ")
from typing import Union, Any

# a = [65,56,89,56,65,89,65,23,23,5,5665,6,865,356,900,8,6,4,889,89,89,56,98]
# max=-1
# sec_max=-1
#
# for k in a:
#     if k>max:
#         max=k
# for n in a:
#     if n<max and n>sec_max:
#         sec_max=n
#
#
# print(max)
# print(sec_max)
import sys
# A=[91,76,81,73,64,13,-63,8,60,27]
# even=-99999999998
# odd=999999999999
# for i in A:
#     if i%2==0:
#         if i>even:
#             even=i
#     else:
#         if i<odd:
#                 odd=i1
# print(even)
# print(odd)
# print(even-odd)
#
# a=[1,2,3]
# b=[]
# print(a+b)

# def fibo(n,memo):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     if n not in memo:
#         memo[n]=fibo(n-1,memo)+fibo(n-2,memo)
#     return memo[n]
#
# mydict={}
# print(fibo(6,mydict))
# a=input().split()
# print(a)
# high=0
# word=""
# for i in a:
#     if len(i)%2==0 and len(i)>high:
#         high=len(i)
#         word=i

# print(word)
# count=0
# def prob(n):
#      global count
#      if n==0:
#
#          return 1
#      if n==1:
#         return 1
#      if n%2!=0:
#         n=n-1
#         return 1+prob(n)
#      if n%2==0:
#         n=n/2
#         return 1+prob(n)
# print(prob(3 ))
# arr=[1,3,4,2,6]
# for i in range(1,len(arr)+1):
# q=[]
# a=int(input())
# for i in range(a):
#     q.append(int(input()))
# count=1
# given=1
# while given<a:
#     if given*2 < a:
#         given*=2
#         count+=1
#     else:
#         given=given+1
#         count+=1
# print(count)

# a=[1,3,5,7,9]
# b=[1,5,9,19,24]
# a_index=0
# b_index=0
# q=[]
# while a_index<len(a) and b_index<len(b):
#     if a[a_index]<b[b_index]:
#         q.append(a[a_index])
#         a_index+=1
#     else:
#         q.append(b[b_index])
#         b_index+=1
#
# if a_index==len(a) and b_index<len(b):
#     q=q+b[b_index:]
# if a_index<len(b) and b_index==len(a):
#     q+=a[a_index:]
# if len(q)%2==0:
#     g=len(q)//2
#     res=(q[g]+q[g-1])/2
# else:
#     g=(len(q)//2)+1
#     res=float(q[g])
# print(q)
# print(res)
# a=[1,2,4,8,16,32,64,128]
# a.sort()
# target=82
# temp=sum(a[0:3])
# for i in range(len(a)-2):
#     start=i+1
#     end=len(a)-1
#     while start<end:
#         k=a[i]+a[start]+a[end]
#         # print(k,a[i],a[start],a[end])
#         if k == target:
#             print(target)
#             break
#         if abs(target-k)<abs(target-temp):
#             temp=k
#         if k<target:
#             start+=1
#         else:
#             end-=1
# print(temp)
# class Solution:
#     def solveSudoku(self,board):
#         import collections
#         rows = collections.defaultdict(list)
#         cols = collections.defaultdict(list)
#         squares = collections.defaultdict(list)
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] != ".":
#                     rows[r].append(int(board[r][c]))
#                     cols[c].append(int(board[r][c]))
#                     squares[(r//3,c//3)].append(int(board[r][c]))
#
#         def isvalid(i, r, c):
#             if i in rows[r] or i in cols[c] or i in squares[(r // 3, c // 3)]:
#                 return False
#             return True
#
#         def sudoko(board):
#             for r in range(9):
#                 for c in range(9):
#                     if board[r][c] == ".":
#                         for i in range(1, 10):
#                             if isvalid(i, r, c):
#                                 board[r][c]=str(i)
#                                 rows[r].append(i)
#                                 cols[c].append(i)
#                                 squares[(r//3,c//3)].append(i)
#                                 if sudoko(board) == True:
#                                     return True
#                                 else:
#                                     board[r][c] = "."
#                                     rows[r].remove(i)
#                                     cols[c].remove(i)
#                                 squares[(r//3,c//3)].remove(i)
#                         return False
#             print(board)
#             return True
#         return(sudoko(board))
# Bharath=Solution()
# print(Bharath.solveSudoku([["5","3",".",".","7",".",".",".","."],
#                      ["6",".",".","1","9","5",".",".","."],
#                      [".","9","8",".",".",".",".","6","."],
#                      ["8",".",".",".","6",".",".",".","3"],
#                      ["4",".",".","8",".","3",".",".","1"],
#                      ["7",".",".",".","2",".",".",".","6"],
#                      [".","6",".",".",".",".","2","8","."],
#                      [".",".",".","4","1","9",".",".","5"],
#                      [".",".",".",".","8",".",".","7","9"]]))

# coin change squares problem
# dp={0:1}
# def f(n):
#     if n in dp:
#         return dp[n]
#     for i in range(1,7):
#         if n-i<0:
#             break
#         dp[n]=dp.get(n,0)+f(n-i)
#     return dp[n]
# print(f(6))
# def st(n):
#     if n==0:
#         return 1
#     if n<0:
#         return 0
#     return st(n-1)+st(n-2)
# print(st(5))
#
# def st(n):
#     if n==0:
#         return 1
#     if n<0:
#         return 0
#     for i in range(1,7):
#         if n-i>=0:
# geeksforgeeks
# def maximumToys(N,A,Q,Queries):
#     for i in Queries:
#         array=A[:] #The array has to be independent of A so create a seperate abject for each array
#         amount=i[0]
#         broken=i[1]
#         i.pop(0)
#         i.pop(0)
#         if broken>0:
#             for k in i:
#                 array.pop(k-1)
#         array.sort()
#         bought=0
#         for item in array:
#             if item<=amount:
#                 bought+=1
#                 amount=amount-item
#             else:
#                 break
#         print(bought)
#
# maximumToys(2,[3,3],1,[[1,0]])

# def count1(s):
#     count=0
#     for i in range(len(s)):
#         low=i
#         high=i
#         while low>-1 and high<len(s) and s[low]==s[high]:
#             count+=1
#             low-=1
#             high+=1
#
#         low=i
#         high=i+1
#         while low>-1 and high<len(s) and s[low]==s[high]:
#             count+=1
#             low-=1
#             high+=1
#     print(count)
# count1("aaa")
# Rotten oranges
# def bfs(x,y,matrix,stack):
#     if x-1>-1 and x-1<len(matrix) and y>-1 and y<len(matrix[0]) and matrix[x-1][y]==1:
#         matrix[x-1][y]=2
#         stack.append([x-1,y])
#     if x+1>-1 and x+1<len(matrix) and y>-1 and y<len(matrix[0]) and matrix[x+1][y]==1:
#         matrix[x+1][y]=2
#         stack.append([x+1,y])
#     if x>-1 and x<len(matrix) and y-1>-1 and y-1<len(matrix[0]) and matrix[x][y-1]==1:
#         matrix[x][y-1] = 2
#         stack.append([x,y-1])
#     if x>-1 and x<len(matrix) and y+1>-1 and y+1<len(matrix[0]) and matrix[x][y+1]==1:
#         matrix[x][y+1]=2
#         stack.append([x,y+1])
#
# def count(matrix):
#     stack=[]
#     flag=True
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j]==2:
#                 stack.append([i,j])
#             if matrix[i][j]==1:
#                 flag=False
#     if flag!=False:
#         return 0
#     # print(stack)
#     time=0
#     while len(stack)>0:
#         print(stack)
#         for i in range(len(stack)):
#             p=stack.pop(0)
#             x,y=p[0],p[1]
#             bfs(x,y,matrix,stack)
#             print("After",time+1, matrix)
#         time=time+1
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j]==1:
#                 return -1
#     return time-1
# print(count([[0,2]]))

# import collections,math
# def encryption(s):
#     # Write your code here
#     dict=collections.defaultdict(list)
#     ans=[]
#     s="".join(s.split())
#     i=math.ceil(len(s)**0.5)
#     print(i)
#     for k in range(len(s)):
#         dict[k%i].append(s[k])
#     for vals in dict:
#         ans.append("".join(dict[vals]))
#     ans1=print(*ans)
#     return str(ans1)
# encryption("haveaniceday")
# buy and sell stock 3
# def prod(mat):
# dup=mat[:]
# ans=[]
# if mat==sorted(mat):
#     return mat[-1]-mat[0]
# elif mat==sorted(mat)[::-1]:
#     return 0
# else:
#     mat=dup[:]
#     for i in range(1,len(mat)):
#         if mat[i-1]<mat[i]:
#             ans.append(mat[i]-mat[i-1])
#     if len(ans)>1:
#         ans.sort()
#         a1=ans[-1]
#         a2=ans[-2]
#         return a1+a2
#     return sum(ans)
# print(prod([6,1,3,2,4,7]))
import sys


# import time
# start_time=time.time()
class Solution:
    def snakesAndLadders(self,board):
        board.reverse()
        def convert(x,length):
            row=x//length
            col=x%length
            if row%2!=0:
                col=length-1-col
            return [row,col]

        def change(board,pos,steps,ans):
            if pos>len(board)*len(board):
                return
            if pos==len(board)*len(board):
                # print(steps)
                ans.append(steps)
                return
            row,col=convert(pos-1,len(board))
            if board[row][col]!=-1:
                change(board,board[row][col],steps,ans)
                return
            for var in range(1,7):
                change(board,pos+var,steps+1,ans)
            return min(ans)
        return change(board,1,0,[])





    # def snakesAndLadders(self, board):
    #     board.reverse()
    #     length = len(board)
    #     ans=[]
    #     def convert(x):
    #         row = (x-1) // length
    #         col = (x-1) % length
    #         if row % 2 != 0:
    #             col = length-1-col   #col=-(length-col)
    #         return [row, col]
    #     queue=[[1,0]]
    #     visit=set()
    #     while len(queue)>0:
    #         pos,steps=queue.pop(0)
    #         for i in range(1,7):
    #             nextsquare=pos+i
    #             if nextsquare==length**2:
    #                 return steps+1
    #             row,col=convert(nextsquare)
    #             if board[row][col]!=-1:
    #                 nextsquare=board[row][col]
    #             if nextsquare not in visit:
    #                 # visit.add(nextsquare)
    #                 queue.append([nextsquare,steps+1])
# C = Solution()
# print(C.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
#                           [-1,-1,-1,-1,-1,-1],
#                           [-1,-1,-1,-1,-1,-1],
#                           [-1,35,-1,-1,13,-1],
#                           [-1,-1,-1,-1,-1,-1],
#                           [-1,15,-1,-1,-1,-1]]))
#leetcode 997
# import collections
# def find(n,trust):
#     dict=collections.defaultdict(list)
#     for p,e in trust:
#         dict[p].append(e)
#     print(len(dict))
#     print(dict)
#     for i in range(1,n+1):
#         flag=True
#         for val in dict.values():
#             if i not in val:
#                 flag=False
#                 break
#         if flag==True:
#             return i
#
#
# print(find(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))
#leetcode
# import collections,heapq
# def findCheapestPrice( n, flights, src, dst, k):
#     dict = collections.defaultdict(list)
#     for source, dest, cost in flights:
#         dict[source].append([dest, cost])
#     print(dict)
#     totalcost = [float("inf") for i in range(n)]
#     visited = set()
#     li = []
#     heapq.heappush(li, [0, src])
#     # visited.add()
#     totalcost[src] = 0
#     steps = 0
#     while steps <   k:
#         for i in range(len(li)):
#             cost, node = heapq.heappop(li)
#             if node not in visited:
#                 visited.add(node)
#                 for nei, time in dict[node]:
#                     if nei not in visited:
#                         totalcost[nei] = min(totalcost[nei], cost + time)
#                         heapq.heappush(li, [totalcost[nei], nei])
#         steps+=1
#     print(totalcost)
#     if totalcost[dst] != float("inf"):
#         return totalcost[dst]
#     return -1
# print(findCheapestPrice(n =4,flights =[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],src =0,dst =3,k =1))
