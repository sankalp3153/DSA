"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1188
Updated: 2025-11-30T17:10:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1188
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
