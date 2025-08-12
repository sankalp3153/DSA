"""
Module: rotate_matrix
Approach: in-place transpose and row reversal
Revision: 831
Updated: 2025-08-12T16:35:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 831
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
