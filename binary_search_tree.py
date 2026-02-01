"""
File Name: binary_search_tree.py

Purpose:
--------
This file contains the implementation of a Binary Search Tree (BST).
In a BST:
- Left subtree contains values smaller than the root
- Right subtree contains values greater than the root

Operations supported:
- Insert
- Search
- Inorder traversal (gives sorted output)

Time Complexity:
----------------
Average Case: O(log n)
Worst Case:   O(n)

Space Complexity:
-----------------
O(n)
"""


class BSTNode:
    def __init__(self, data):
        # Store node value
        self.data = data
        # Left child
        self.left = None
        # Right child
        self.right = None


class BinarySearchTree:
    def insert(self, root, data):
        # If tree is empty, create new node
        if root is None:
            return BSTNode(data)

        # Insert in left subtree
        if data < root.data:
            root.left = self.insert(root.left, data)

        # Insert in right subtree
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        # If root is null or key found
        if root is None or root.data == key:
            return root

        # Search left subtree
        if key < root.data:
            return self.search(root.left, key)

        # Search right subtree
        return self.search(root.right, key)

    def inorder(self, root):
        # Inorder traversal gives sorted order
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# ------------------ Example Usage ------------------

bst = BinarySearchTree()
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = bst.insert(root, v)

print("Inorder Traversal (Sorted):")
bst.inorder(root)

key = 60
print("\nSearch", key, ":", "Found" if bst.search(root, key) else "Not Found")
