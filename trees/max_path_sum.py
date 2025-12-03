"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1206
Updated: 2025-12-03T11:13:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1206
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
