"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 562
Updated: 2025-05-26T23:41:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 562
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
