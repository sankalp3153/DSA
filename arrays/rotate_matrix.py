"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1268
Updated: 2025-12-18T18:31:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1268
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
