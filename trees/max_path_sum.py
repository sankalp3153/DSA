"""
Binary Tree Maximum Path Sum using post-order gain recursion.
Time: O(n) | Space: O(h)
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)
        best = max(best, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return int(best)
