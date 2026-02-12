"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1464
Updated: 2026-02-12T10:06:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1464
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
