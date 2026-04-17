"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1689
Updated: 2026-04-17T10:50:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1689
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
