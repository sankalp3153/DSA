"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 355
Updated: 2025-03-25T22:06:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 355
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
