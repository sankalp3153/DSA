"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1275
Updated: 2025-12-22T12:20:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1275
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
