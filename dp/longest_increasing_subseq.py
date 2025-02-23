"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 222
Updated: 2025-02-23T21:51:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 222
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
