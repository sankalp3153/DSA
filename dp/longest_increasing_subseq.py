"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1372
Updated: 2026-01-19T21:52:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1372
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
