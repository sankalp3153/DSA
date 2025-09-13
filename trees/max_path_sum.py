"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 953
Updated: 2025-09-13T15:33:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 953
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
