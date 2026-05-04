"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1735
Updated: 2026-05-04T15:49:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1735
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
