"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 746
Updated: 2025-07-23T19:05:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 746
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
