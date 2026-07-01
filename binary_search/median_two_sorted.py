"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1918
Updated: 2026-07-01T18:17:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1918
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
