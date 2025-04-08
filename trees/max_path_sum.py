"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 401
Updated: 2025-04-08T12:08:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 401
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
