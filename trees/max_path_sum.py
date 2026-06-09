"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1850
Updated: 2026-06-09T16:21:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1850
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
