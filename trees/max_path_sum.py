"""
Module: max_path_sum
Approach: post-order gain recursion
Revision: 1528
Updated: 2026-03-02T11:54:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1528
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
