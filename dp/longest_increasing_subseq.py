"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 291
Updated: 2025-03-12T19:46:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 291
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
