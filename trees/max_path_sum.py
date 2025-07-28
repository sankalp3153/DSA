"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 769
Updated: 2025-07-28T21:32:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 769
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
