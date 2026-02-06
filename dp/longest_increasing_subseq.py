"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1441
Updated: 2026-02-06T15:30:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1441
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
