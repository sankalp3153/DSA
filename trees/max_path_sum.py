"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 332
Updated: 2025-03-21T17:24:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 332
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
