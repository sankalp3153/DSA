"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 999
Updated: 2025-09-26T21:33:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 999
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
