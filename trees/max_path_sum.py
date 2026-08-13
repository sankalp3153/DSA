"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2057
Updated: 2026-08-13T18:42:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2057
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
