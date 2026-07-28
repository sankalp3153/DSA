"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2011
Updated: 2026-07-28T19:45:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2011
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
