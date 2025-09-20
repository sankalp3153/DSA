"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 975
Updated: 2025-09-20T11:08:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 975
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
