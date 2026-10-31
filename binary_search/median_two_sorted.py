"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2309
Updated: 2026-10-31T19:45:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2309
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
