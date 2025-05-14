"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 516
Updated: 2025-05-14T15:53:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 516
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
