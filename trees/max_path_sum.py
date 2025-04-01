"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 378
Updated: 2025-04-01T21:08:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 378
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
