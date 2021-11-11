import sys

class Tree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = self.Node("A")

    def put(self, target, left=None, right=None):
        left = None if left == "." else left
        right = None if right == "." else right
        self.put_recursive(self.root,target,left,right)

    def put_recursive(self, current, target, left, right):
        if current.data == target:
            current.left = self.Node(left) if left else None
            current.right = self.Node(right) if right else None
            return
        if current.left:
            self.put_recursive(current.left,target,left,right)
        if current.right:
            self.put_recursive(current.right,target,left,right)

    def preorder(self, target=None):
        if not target:
            self.preorder(self.root)
            return
        print(target.data, end="")
        if target.left:
            self.preorder(target.left)
        if target.right:
            self.preorder(target.right)

    def inorder(self, target=None):
        if not target:
            self.inorder(self.root)
            return
        if target.left:
            self.inorder(target.left)
        print(target.data, end="")
        if target.right:
            self.inorder(target.right)

    def postorder(self, target=None):
        if not target:
            self.postorder(self.root)
            return
        if target.left:
            self.postorder(target.left)
        if target.right:
            self.postorder(target.right)
        print(target.data, end="")

n = int(sys.stdin.readline().strip())

tree = Tree()

for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    tree.put(parent, left, right)

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()