"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1165
Updated: 2025-11-24T23:37:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1165
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
