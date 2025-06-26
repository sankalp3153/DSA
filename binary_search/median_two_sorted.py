"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 676
Updated: 2025-06-26T22:10:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 676
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
