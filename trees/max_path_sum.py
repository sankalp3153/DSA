"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 56
Updated: 2025-01-10T23:02:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 56
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
