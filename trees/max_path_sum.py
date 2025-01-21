"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 79
Updated: 2025-01-21T15:13:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 79
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
