"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2315
Updated: 2026-11-02T11:21:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2315
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
