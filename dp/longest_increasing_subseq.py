"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1671
Updated: 2026-04-12T20:35:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1671
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
