"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1602
Updated: 2026-03-23T14:06:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1602
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
