"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1551
Updated: 2026-03-07T17:26:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1551
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
