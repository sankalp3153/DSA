"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1459
Updated: 2026-02-10T17:23:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1459
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
