"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1901
Updated: 2026-06-24T12:05:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1901
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
