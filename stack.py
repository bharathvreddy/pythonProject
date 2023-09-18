# #SUCCESSFULLY DONE
# class stack:
#     def __init__(self):
#         self.list=[]
#
#     def isEmpty(self):
#         if self.list==[]:
#             return "True"
#
#     def push(self,value):
#         self.list.append(value)
#         return "Successfully executed"
#
#     def pop(self):
#         if self.list==[]:
#             return "Empty,cant pop"
#         print(self.list.pop())
#
#     def peek(self):
#         if self.list==[]:
#             return "No peek"
#         return self.list[len(self.list)-1]
#
#
# Customstack=stack()
# print(Customstack.isEmpty())
# Customstack.push(1)
# Customstack.push(2)
# Customstack.push(3)
# print()
# Customstack.pop() #will delete the element which has inserted into list at last
# print()
# print(Customstack.peek())
#
#
# print("queue")
# print()
#
# #QUEUE
#
#
# class queue:
#     def __init__(self):
#         self.list=[]
#
#
#     def enqueue(self,value):
#         self.list.append(value)
#     def dequeue(self):
#         self.list.pop(0)
#     def peek(self):
#         print(self.list[len(self.list)-1])
#     def display(self):
#         for c in self.list:
#             print(c)
#
#
# q=queue()
# q.enqueue(0)
# q.enqueue(1)
# q.enqueue(2)
# q.display()
# q.dequeue()
# print()
# q.display()
# print()
# q.peek()
# max1=float("inf")
# kavali=0
# kr=[]
# def maxgrid(array,i,j,ds,total):
#     global max1,kavali,kr
#     if i==0 and j==0:
#         ds.append(array[0][0])
#         total+=array[0][0]
#         if total<max1:
#             max1=total
#             kavali=max(ds)
#             kr=ds[:]
#         return
#     if i<0 or j<0:
#         return float("-inf")
#
#     left=maxgrid(array,i,j-1,ds+[array[i][j]],total+array[i][j])
#     up=maxgrid(array,i-1,j,ds+[array[i][j]],total+array[i][j])
#     return kavali,kr,max1

# print(maxgrid([[4,2,11,10],[6,7,1,9],[5,12,3,8]],2,3,[],0))
# print(6>>3 and 1)
# class node:
#     def __init__(self,val,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
#
# a=node(1)
# b=node(2)
# c=node(3)
# d=node(4)
# e=node(42)
# f=node(11)
# a.left=b
# b.right=e
# a.right=c
# c.right=d
# d.left=f
#LEVEL ORDER TRAVERSAL -LEFT VIEW
# def left(root):
#     if not root:
#         return []
#     queue=[root,None]
#     ans=[]
#     prev=None
#     while len(queue)>1:
#         q=queue.pop(0)
#         if q is None:
#             queue.append(None)
#             prev = None
#             continue
#         if prev==None:
#             ans.append(q.val)
#         # if prev==None:
#         #     ans.append(q.val)
#         if q.left is not None:
#             queue.append(q.left)
#         if q.right is not None:
#             queue.append(q.right)
#         prev=q
#
#     return ans
# print(left(a))

# def left(root,sum):
#     if root is None:
#         return
#     if root.left is None and root.right is None:
#         print(sum+root.val)
#         return
#     left(root.left,sum+root.val)
#     left(root.right,sum+root.val)
# left(a,0)
# from collections import Counter
# k=Counter("fgrydcjjhgrj")
# print(k)
# import math
# print(math.ceil(2))

# costs = [1,3,2,4,1]
# costs.sort()
# coins=7
# dp=[[0 for i in range(coins+1)] for k in range(len(costs))]
# def f(coins,index):
#     if coins<costs[0]:
#         return 0
#     if index==0:
#         if coins>=costs[0]:
#             return 1
#         return 0
#     nottake=0+f(coins,index-1)
#     take=float("-inf")
#     if coins>=costs[index]:
#         take=1+f(coins-costs[index],index-1)
#     return max(take,nottake)
# print(f(7,4))
# dp=[[0 for i in range(coins+1)] for k in range(len(costs))]
# def f1(coins,index):
#     k=costs[0]
#     for i in range(len(dp[0])):
#         if i>=k:
#             dp[0][i]=1
#     for index in range(1,len(dp)):
#         for coins in range(len(dp[0])):
#             nottake=dp[index-1][coins]
#             take=float("-inf")
#             if coins>=costs[index]:
#                 take=1+dp[index-1][coins-costs[index]]
#             dp[index][coins]=max(take,nottake)
#     return dp[-1][-1]
# print(f1(7,4))

# matrix=[[1,0,0,0,1,0],[1,0,0,1,0,1],[0,0,1,0,1,0],[1,0,1,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,1]]
# def dfs(matrix,i,j):
#     if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]==0:
#         return
#     matrix[i][j]=0
#     dfs(matrix,i-1,j)
#     dfs(matrix,i+1,j)
#     dfs(matrix,i,j-1)
#     dfs(matrix,i,j+1)
#
# count=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==1:
#             dfs(matrix,i,j)
#             count+=1
# print(count)
#geeksforgeeks
# def minIncrements(arr,N):
#     # Code here
#     arr.sort()
#     prev = arr[0]
#     count = 0
#     for i in range(1, len(arr)):
#         if arr[i] > prev:
#             prev = arr[i]
#             continue
#         else:
#             diff = abs(prev - arr[i])
#             count += diff + 1
#             arr[i] = arr[i] + diff + 1
#             prev = arr[i]
#     return count
# print(minIncrements([1,3,3,3,4,4,5,6,7],9))

# graph = {
#   '5' : ['3','7'],
#   '3' : ['2','4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }
#
# visited = set() # Set to keep track of visited nodes of graph.
#all paths in a graph
# def dfs(visited, graph, node,temp):  #function for dfs
#     if node not in visited:
#         temp.append(node)
#         # print(node)
#         visited.add(node)
#         for n in graph[node]:
#             if n not in visited:
#                 break
#         else:
#             print(temp)
#             return
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour,temp)
#             # print(temp)
#             temp.pop()
#
# # Driver Code
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5',[])

# def setZeros(List):
# 	# Write your code here.
#     add=[]
#     for row in range(len(List)):
#         for col in range(len(List[0])):
#             if List[row][col]==0:
#                 add.append([row,col])
#     for row,col in add:
#         for i in range(len(List)):
#             List[i][col] = 0
#         for i in range(len(List[0])):
#             List[row][i] = 0
#
#
#     return List
# print(setZeros([[1, 2, 3],[4, 0, 6],[7 ,8 ,9]]))

# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
#
# N1=Node(1)
# N2=Node(2)
# N3=Node(3)
# N4=Node(4)
# N5=Node(5)
# N6=Node(6)
# N1.next=N2
# N2.next=N3
# N3.next=N4
# N4.next=N5
# N5.next=N6
# h1=N1
# h2=None
# while h1 is not None:
#     temp=h1
#     h1=h1.next
#     temp.next=h2
#     h2=temp
#
#
# while h2 is not None:
#     print(h2.val)
#     h2=h2.next



# while starter is not None:
#     print(starter.val)
#     starter=starter.next


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