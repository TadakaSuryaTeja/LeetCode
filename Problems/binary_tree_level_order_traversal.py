# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(k):
            if len(k) == 0:
                return
            ans, temp_val = [], []
            for node in k:
                ans.append(node.val)

                if node.left:
                    temp_val.append(node.left)
                if node.right:
                    temp_val.append(node.left)

            res.append(ans)
            solve(temp_val)
            return

        res = []
        if root:
            solve([root])
        return res
