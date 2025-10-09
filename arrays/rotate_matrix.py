"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 1038
Updated: 2025-10-09T14:18:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1038
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
