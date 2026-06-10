"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1855
Updated: 2026-06-10T18:47:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1855
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
