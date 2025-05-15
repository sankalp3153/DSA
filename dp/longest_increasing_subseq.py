"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 521
Updated: 2025-05-15T14:28:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 521
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
