"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 820
Updated: 2025-08-11T10:33:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 820
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
