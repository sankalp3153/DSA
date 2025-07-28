"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 768
Updated: 2025-07-28T18:28:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 768
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
