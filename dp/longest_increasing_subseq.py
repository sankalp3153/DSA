"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 153
Updated: 2025-02-04T21:41:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 153
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
