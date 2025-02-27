# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        Given the root of a binary tree, return the sum of every tree node's tilt.
        """
        pass  # Your code here


# Test Case 1
root1 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
# Expected output: 12

# Test Case 2
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
# Expected output: 1

# Test Case 3
root3 = None
# Expected output: 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        Given the root of a binary tree, return the sum of every tree node's tilt.
        """
        total_tilt = 0

        def subtree_sum(node):
            nonlocal total_tilt
            if not node:
                return 0

            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)

            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            return node.val + left_sum + right_sum

        subtree_sum(root)
        return total_tilt
