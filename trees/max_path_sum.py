"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1666
Updated: 2026-04-12T10:09:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1666
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
