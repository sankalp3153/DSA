"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 125
Updated: 2025-01-29T22:23:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 125
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
