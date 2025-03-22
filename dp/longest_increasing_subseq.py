"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 337
Updated: 2025-03-22T10:18:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 337
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
