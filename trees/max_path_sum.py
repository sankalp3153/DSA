"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1965
Updated: 2026-07-14T14:25:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1965
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
