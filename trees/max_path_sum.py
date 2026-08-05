"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2034
Updated: 2026-08-05T17:57:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2034
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
