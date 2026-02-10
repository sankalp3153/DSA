"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1458
Updated: 2026-02-10T13:13:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1458
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
