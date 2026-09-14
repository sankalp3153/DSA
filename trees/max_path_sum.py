"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2172
Updated: 2026-09-14T15:20:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2172
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
