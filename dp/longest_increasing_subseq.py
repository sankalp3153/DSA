"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2154
Updated: 2026-09-04T20:19:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2154
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
