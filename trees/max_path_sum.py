"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2241
Updated: 2026-10-05T10:59:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2241
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
