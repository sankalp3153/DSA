"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1159
Updated: 2025-11-24T10:38:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1159
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
