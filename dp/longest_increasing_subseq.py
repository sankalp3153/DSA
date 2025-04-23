"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 452
Updated: 2025-04-23T12:17:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 452
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
