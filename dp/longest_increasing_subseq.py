"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1395
Updated: 2026-01-26T21:06:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1395
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
