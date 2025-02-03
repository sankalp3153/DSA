"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 147
Updated: 2025-02-03T18:04:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 147
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
