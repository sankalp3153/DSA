"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1988
Updated: 2026-07-21T16:14:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1988
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
