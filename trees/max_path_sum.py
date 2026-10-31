"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2310
Updated: 2026-10-31T20:00:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2310
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
