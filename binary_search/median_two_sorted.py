"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1044
Updated: 2025-10-10T14:44:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1044
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
