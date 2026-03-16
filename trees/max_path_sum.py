"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1574
Updated: 2026-03-16T13:42:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1574
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
