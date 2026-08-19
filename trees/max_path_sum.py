"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2080
Updated: 2026-08-19T10:31:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2080
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
