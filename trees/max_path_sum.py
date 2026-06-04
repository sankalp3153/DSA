"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1827
Updated: 2026-06-04T15:06:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1827
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
