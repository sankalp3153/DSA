"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 838
Updated: 2025-08-13T14:22:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 838
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
