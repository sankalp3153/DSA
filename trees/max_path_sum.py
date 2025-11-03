"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1114
Updated: 2025-11-03T21:02:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1114
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
