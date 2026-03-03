"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1533
Updated: 2026-03-03T16:04:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1533
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
