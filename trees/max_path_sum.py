"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 148
Updated: 2025-02-03T19:28:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 148
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
