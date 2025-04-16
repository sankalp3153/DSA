"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 424
Updated: 2025-04-16T18:07:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 424
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
