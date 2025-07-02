"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 693
Updated: 2025-07-02T20:26:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 693
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
