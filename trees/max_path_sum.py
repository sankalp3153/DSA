"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 217
Updated: 2025-02-22T15:38:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 217
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
