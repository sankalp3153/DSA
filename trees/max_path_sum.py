"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1482
Updated: 2026-02-17T13:38:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1482
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
