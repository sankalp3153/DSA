"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 463
Updated: 2025-04-25T19:02:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 463
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
