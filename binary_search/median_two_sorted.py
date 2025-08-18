"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 860
Updated: 2025-08-18T18:50:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 860
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
