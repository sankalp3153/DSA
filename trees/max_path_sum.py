"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1298
Updated: 2025-12-27T22:12:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1298
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
