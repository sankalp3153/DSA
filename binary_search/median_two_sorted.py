"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 400
Updated: 2025-04-07T18:56:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 400
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
