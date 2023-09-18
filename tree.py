class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    def relation(self, left, right):

        self.left = left
        self.right = right

def preOrderTraversal(root):
    if root==None:
        return 1
    print(root.data)
    retVal = preOrderTraversal(root.left)
    retVal = preOrderTraversal(root.right)

#preOrderTraversal(Drinks)-> preOrderTraversal(Hot) and preOrderTraversal(Cold)
#
#
#
#
#

Drinks = TreeNode("Drinks")
Hot = TreeNode("Hot")
Cold = TreeNode("Cold")
Coffee = TreeNode("Coffee")
Tea = TreeNode("Tea")
Cola = TreeNode("Cola")
Fanta = TreeNode("Fanta")
Drinks.relation(Hot, Cold)
Hot.relation(Coffee, Tea)
Cold.relation(Cola, Fanta)

preOrderTraversal(Drinks)