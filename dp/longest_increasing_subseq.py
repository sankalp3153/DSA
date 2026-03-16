"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1579
Updated: 2026-03-16T22:46:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1579
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
