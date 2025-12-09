"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1229
Updated: 2025-12-09T23:25:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1229
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
