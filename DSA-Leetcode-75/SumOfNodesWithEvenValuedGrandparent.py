# 1315. Sum of Nodes with Even-Valued Grandparent
## Not a part of Leetcode Blind 75
'''
Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.
A grandparent of a node is the parent of its parent if it exists.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumEvenGrandparent(root) -> int:
    bfs = [(root, -1, -1)]
    even_sum = 0
    while len(bfs) > 0:
        node, parent, grandparent = bfs.pop(0)
        if grandparent % 2 == 0:
            even_sum += node.val
        if node.left:
            bfs.append((node.left, node.val, parent))
        if node.right:
            bfs.append((node.right, node.val, parent))
    return even_sum