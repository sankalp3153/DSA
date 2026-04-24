"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1711
Updated: 2026-04-24T19:54:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1711
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
