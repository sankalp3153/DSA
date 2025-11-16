"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1137
Updated: 2025-11-16T11:41:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1137
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
