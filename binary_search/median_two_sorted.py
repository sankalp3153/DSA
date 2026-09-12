"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2171
Updated: 2026-09-12T12:36:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2171
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
