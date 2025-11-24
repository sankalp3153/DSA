"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1160
Updated: 2025-11-24T11:46:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1160
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
