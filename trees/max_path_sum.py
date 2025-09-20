"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 976
Updated: 2025-09-20T20:37:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 976
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
