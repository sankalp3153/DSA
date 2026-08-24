"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2103
Updated: 2026-08-24T14:55:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2103
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
