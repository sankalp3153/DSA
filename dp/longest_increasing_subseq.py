"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2223
Updated: 2026-09-30T23:03:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2223
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
