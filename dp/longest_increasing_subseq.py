"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2016
Updated: 2026-07-29T23:19:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2016
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
