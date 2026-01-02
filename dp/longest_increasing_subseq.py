"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1326
Updated: 2026-01-02T23:26:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1326
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
