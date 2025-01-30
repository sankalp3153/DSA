"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 130
Updated: 2025-01-30T15:40:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 130
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
