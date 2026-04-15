# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        start_root = root

        # handle empty tree / last leaf
        if root is None:
            return None

        # recurentially invert leafs
        left_inv = self.invertTree(root.left)
        right_inv = self.invertTree(root.right)

        # do the actual inversion of not-None leafs:
        root.left, root.right = right_inv, left_inv

        # return the root for output & recurrence
        return root