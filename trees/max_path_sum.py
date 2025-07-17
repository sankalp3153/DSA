"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 723
Updated: 2025-07-17T13:40:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 723
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
