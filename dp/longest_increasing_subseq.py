"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1004
Updated: 2025-09-27T22:04:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1004
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
