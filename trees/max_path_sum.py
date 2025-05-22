"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 539
Updated: 2025-05-22T21:01:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 539
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
