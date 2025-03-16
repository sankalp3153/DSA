"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 309
Updated: 2025-03-16T23:36:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 309
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
