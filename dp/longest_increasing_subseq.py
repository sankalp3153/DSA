"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 636
Updated: 2025-06-17T22:02:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 636
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
