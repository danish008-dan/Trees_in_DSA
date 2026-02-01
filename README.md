Binary Tree - Python
====================

Overview
--------
A Binary Tree is a hierarchical data structure where each node
has at most two children: left and right.

Binary Trees are the foundation for advanced tree structures
such as Binary Search Trees, Heaps, and AVL Trees.

Tree Traversals
---------------
1. Inorder Traversal   (Left, Root, Right)
2. Preorder Traversal  (Root, Left, Right)
3. Postorder Traversal (Left, Right, Root)

Time Complexity
---------------
Traversal: O(n)

Space Complexity
----------------
O(n)

Use Cases
---------
- Expression trees
- Hierarchical data representation
- Foundation for advanced trees


Binary Search Tree - Python
===========================

Overview
--------
A Binary Search Tree (BST) is a special type of binary tree
that maintains ordered data.

BST Property
------------
- Left subtree values < root value
- Right subtree values > root value

Operations
----------
- Insert
- Search
- Traversal

Time Complexity
---------------
Average Case: O(log n)
Worst Case:   O(n)

Space Complexity
----------------
O(n)

Advantages
----------
- Faster search compared to arrays
- Inorder traversal gives sorted data

Disadvantages
-------------
- Can become skewed
- Performance degrades without balancing

Use Cases
---------
- Searching and sorting
- Database indexing
- File systems
