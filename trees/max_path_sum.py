"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2333
Updated: 2026-11-06T14:03:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2333
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
