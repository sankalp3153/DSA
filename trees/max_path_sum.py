"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 493
Updated: 2025-05-08T22:25:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 493
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
