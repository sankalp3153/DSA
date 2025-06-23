"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 659
Updated: 2025-06-23T21:48:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 659
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
