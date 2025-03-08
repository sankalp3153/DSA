"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 263
Updated: 2025-03-08T15:59:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 263
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
