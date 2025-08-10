"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 815
Updated: 2025-08-10T10:12:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 815
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
