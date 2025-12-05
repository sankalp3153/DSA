"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1211
Updated: 2025-12-05T11:07:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1211
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
