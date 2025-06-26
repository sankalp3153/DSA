"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 670
Updated: 2025-06-26T14:59:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 670
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
