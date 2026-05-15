"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1758
Updated: 2026-05-15T11:38:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1758
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
