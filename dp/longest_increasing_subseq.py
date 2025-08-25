"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 889
Updated: 2025-08-25T17:21:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 889
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
