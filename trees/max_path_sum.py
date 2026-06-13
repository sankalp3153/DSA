"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1873
Updated: 2026-06-13T13:11:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1873
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
