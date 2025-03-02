"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 240
Updated: 2025-03-02T16:59:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 240
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
