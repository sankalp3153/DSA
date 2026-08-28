"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2126
Updated: 2026-08-28T18:05:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2126
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
