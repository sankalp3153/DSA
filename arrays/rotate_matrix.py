"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 440
Updated: 2025-04-18T19:52:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 440
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
