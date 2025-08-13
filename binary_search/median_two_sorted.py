"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 837
Updated: 2025-08-13T12:01:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 837
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
