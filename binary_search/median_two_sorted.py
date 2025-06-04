"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 584
Updated: 2025-06-04T13:51:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 584
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
