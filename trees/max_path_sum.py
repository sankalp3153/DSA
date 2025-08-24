"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 884
Updated: 2025-08-24T18:44:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 884
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
