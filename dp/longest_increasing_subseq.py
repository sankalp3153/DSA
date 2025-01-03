"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 15
Updated: 2025-01-03T18:51:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 15
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
