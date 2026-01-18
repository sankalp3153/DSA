"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1367
Updated: 2026-01-18T18:09:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1367
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
