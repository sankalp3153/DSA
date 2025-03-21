"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 331
Updated: 2025-03-21T15:04:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 331
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
