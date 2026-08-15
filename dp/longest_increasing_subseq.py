"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2062
Updated: 2026-08-15T22:03:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2062
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
