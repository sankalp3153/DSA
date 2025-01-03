"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 9
Updated: 2025-01-03T13:08:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 9
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
