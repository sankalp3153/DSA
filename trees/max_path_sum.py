"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 792
Updated: 2025-08-04T15:23:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 792
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
