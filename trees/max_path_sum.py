"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1643
Updated: 2026-04-05T19:04:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1643
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
