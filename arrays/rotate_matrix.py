"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 187
Updated: 2025-02-13T17:17:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 187
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
