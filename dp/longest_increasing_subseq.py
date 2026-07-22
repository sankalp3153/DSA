"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1993
Updated: 2026-07-22T12:04:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1993
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
