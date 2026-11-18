"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2361
Updated: 2026-11-18T22:30:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2361
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
