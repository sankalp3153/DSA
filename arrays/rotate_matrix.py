"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 3
Updated: 2025-01-02T16:27:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 3
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
