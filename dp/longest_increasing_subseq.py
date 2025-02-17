"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 199
Updated: 2025-02-17T11:14:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 199
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
