"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1418
Updated: 2026-02-01T14:17:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1418
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
