"""
File Name: avl_tree.py

Purpose:
--------
AVL Tree is a self-balancing Binary Search Tree.
The height difference between left and right subtree
is at most 1 for every node.

This guarantees O(log n) time for operations.
"""


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    return node.height if node else 0


def get_balance(node):
    return height(node.left) - height(node.right) if node else 0


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))

    balance = get_balance(root)

    # Left Left
    if balance > 1 and key < root.left.data:
        return right_rotate(root)

    # Right Right
    if balance < -1 and key > root.right.data:
        return left_rotate(root)

    # Left Right
    if balance > 1 and key > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left
    if balance < -1 and key < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

