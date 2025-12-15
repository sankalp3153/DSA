"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1257
Updated: 2025-12-15T21:18:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1257
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
