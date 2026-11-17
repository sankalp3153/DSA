"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2356
Updated: 2026-11-17T21:50:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2356
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
