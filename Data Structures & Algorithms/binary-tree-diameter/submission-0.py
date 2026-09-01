# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def height1(node):
            nonlocal diameter
            if node is None:
                return 0
            left_height=height1(node.left)
            right_height=height1(node.right)
            diameter=max(diameter,left_height+right_height)

            height=1+max(left_height, right_height)
            return height
        height1(root)
        return diameter
        