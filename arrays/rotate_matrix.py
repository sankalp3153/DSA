"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 992
Updated: 2025-09-23T22:23:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 992
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
