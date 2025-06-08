"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 601
Updated: 2025-06-08T21:17:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 601
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
