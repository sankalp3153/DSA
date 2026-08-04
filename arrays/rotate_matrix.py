"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2027
Updated: 2026-08-04T13:25:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2027
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
