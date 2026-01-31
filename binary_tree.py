"""
File Name: binary_tree.py

Purpose:
--------
This file contains the implementation of a Binary Tree.
In a Binary Tree, each node can have at most two children:
- Left child
- Right child

This file also demonstrates tree traversals:
- Inorder
- Preorder
- Postorder

Time Complexity:
----------------
Traversal: O(n)

Space Complexity:
-----------------
O(n)
"""


class Node:
    def __init__(self, data):
        # Store node data
        self.data = data
        # Pointer to left child
        self.left = None
        # Pointer to right child
        self.right = None


class BinaryTree:
    def __init__(self):
        # Initialize root of the tree
        self.root = None

    def inorder(self, node):
        # Left -> Root -> Right
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        # Root -> Left -> Right
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        # Left -> Right -> Root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


# ------------------ Example Usage ------------------

bt = BinaryTree()

bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

print("Inorder Traversal:")
bt.inorder(bt.root)

print("\nPreorder Traversal:")
bt.preorder(bt.root)

print("\nPostorder Traversal:")
bt.postorder(bt.root)
