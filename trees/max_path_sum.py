"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1390
Updated: 2026-01-25T22:41:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1390
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
