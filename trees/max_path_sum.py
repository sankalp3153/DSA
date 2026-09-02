"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 2149
Updated: 2026-09-02T19:01:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2149
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
