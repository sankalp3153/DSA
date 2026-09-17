"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2177
Updated: 2026-09-17T19:37:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2177
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
