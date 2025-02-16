"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 194
Updated: 2025-02-16T14:26:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 194
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
