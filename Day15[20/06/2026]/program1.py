'''class TreeNode:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None

    def insert(self,root=50,value=30):
        Node = TreeNode(value) #TreeNode(30)
        if root is None:
            return Node
        #comapare
        if val<root.value:
            root.left=self.insert(root.left,value=30)
        elif val>root.value:
            root.right=self.insert(root.right,value=70)
        return root 
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.value)
            self.Inorder(root.right)
bst=BST()
root=None
for i in[50,30,20,70,80]:
    root=bst.insert(root,i)
bst.Inorder(root)'''

'''class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return TreeNode(value)

        if value < root.value:
            root.left = self.insert(root.left, value)

        elif value > root.value:
            root.right = self.insert(root.right, value)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)


# Driver code
bst = BST()
root = None

for i in [50, 30, 20, 70, 80]:
    root = bst.insert(root, i)

print("Inorder Traversal:")
bst.inorder(root)'''

'''class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):   # FIX 1: removed default wrong values
        Node = TreeNode(value)

        if root is None:
            return Node

        # compare
        if value < root.value:   # FIX 2: val → value
            root.left = self.insert(root.left, value)   # FIX 3: remove 30

        elif value > root.value:  # FIX 4: val → value
            root.right = self.insert(root.right, value)  # FIX 5: remove 70

        return root

    def Inorder(self, root):
        if root:
            self.Inorder(root.left)
            print(root.value)
            self.Inorder(root.right)


bst = BST()
root = None

for i in [50, 30, 20, 70, 80]:
    root = bst.insert(root, i)

bst.Inorder(root)'''


'''class Solution:
    def inorderTraversal(self, root):
      

        def inorder(root,res):
            if root:
                inorder(root.left,result)      
                result.append(root.value) 
                inorder(root.right,res) 
            return res
        return inorder(root,[])'''

class Solution:
    def PreorderTraversal(self, root):
      

        def preorder(root,res):
            if root:
                preorder(root.left,right)      
                result.append(root.value) 
                preorder(root.right,res) 
            return res
        return preorder(root,[]) 