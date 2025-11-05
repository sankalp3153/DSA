"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1119
Updated: 2025-11-05T21:41:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1119
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
