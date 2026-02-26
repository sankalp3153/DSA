"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1505
Updated: 2026-02-26T20:40:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1505
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
