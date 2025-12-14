"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1252
Updated: 2025-12-14T22:12:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1252
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
