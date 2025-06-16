"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 631
Updated: 2025-06-16T15:30:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 631
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
