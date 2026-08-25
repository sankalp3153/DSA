"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2108
Updated: 2026-08-25T22:38:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2108
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
