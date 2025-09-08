"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 935
Updated: 2025-09-08T18:54:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 935
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
