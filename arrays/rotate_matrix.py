"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 877
Updated: 2025-08-23T18:20:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 877
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
