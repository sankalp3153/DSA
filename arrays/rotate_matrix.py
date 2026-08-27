"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 2119
Updated: 2026-08-27T16:47:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2119
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
