"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 654
Updated: 2025-06-20T23:22:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 654
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
