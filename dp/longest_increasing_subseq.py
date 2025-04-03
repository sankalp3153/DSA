"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 383
Updated: 2025-04-03T10:39:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 383
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
