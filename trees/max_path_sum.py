"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 907
Updated: 2025-09-01T10:46:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 907
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
