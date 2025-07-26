"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 762
Updated: 2025-07-26T19:40:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 762
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
