"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 302
Updated: 2025-03-16T16:25:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 302
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
