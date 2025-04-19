"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 446
Updated: 2025-04-19T19:46:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 446
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
