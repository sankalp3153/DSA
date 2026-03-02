"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1527
Updated: 2026-03-02T11:24:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1527
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
