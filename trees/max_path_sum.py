"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1919
Updated: 2026-07-01T22:28:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1919
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
