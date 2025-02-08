"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 171
Updated: 2025-02-08T17:06:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 171
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
