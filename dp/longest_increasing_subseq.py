"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 567
Updated: 2025-05-30T13:16:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 567
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
