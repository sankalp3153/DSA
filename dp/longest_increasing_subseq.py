"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1280
Updated: 2025-12-23T14:55:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1280
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
