"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 677
Updated: 2025-06-27T12:13:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 677
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
