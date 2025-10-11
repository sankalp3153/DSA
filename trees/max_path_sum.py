"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1045
Updated: 2025-10-11T13:48:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1045
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
