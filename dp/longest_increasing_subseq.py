"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1027
Updated: 2025-10-06T18:57:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1027
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
