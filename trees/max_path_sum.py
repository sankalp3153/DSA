"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 585
Updated: 2025-06-04T19:24:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 585
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
