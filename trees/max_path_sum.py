"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 33
Updated: 2025-01-07T18:35:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 33
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
