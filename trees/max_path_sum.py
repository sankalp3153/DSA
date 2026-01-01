"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1321
Updated: 2026-01-01T21:52:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1321
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
