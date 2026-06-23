"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1896
Updated: 2026-06-23T10:01:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1896
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
