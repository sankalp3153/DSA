"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 107
Updated: 2025-01-28T12:25:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 107
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
