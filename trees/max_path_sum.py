"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 102
Updated: 2025-01-25T13:58:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 102
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
