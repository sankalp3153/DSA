"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 700
Updated: 2025-07-07T18:53:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 700
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
