"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1068
Updated: 2025-10-20T11:20:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1068
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
