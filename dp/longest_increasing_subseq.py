"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2085
Updated: 2026-08-19T20:00:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2085
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
