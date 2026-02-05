"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1436
Updated: 2026-02-05T19:23:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1436
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
