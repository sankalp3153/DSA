"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1781
Updated: 2026-05-20T10:31:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1781
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
