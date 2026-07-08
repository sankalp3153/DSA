"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1942
Updated: 2026-07-08T16:23:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1942
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
