"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 470
Updated: 2025-04-30T23:02:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 470
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
