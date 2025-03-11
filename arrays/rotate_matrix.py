"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 279
Updated: 2025-03-11T13:52:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 279
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
