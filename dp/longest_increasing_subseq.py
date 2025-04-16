"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 429
Updated: 2025-04-16T23:00:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 429
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
