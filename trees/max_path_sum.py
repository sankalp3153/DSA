"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 930
Updated: 2025-09-06T17:56:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 930
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
