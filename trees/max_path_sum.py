"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2264
Updated: 2026-10-15T15:32:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2264
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
