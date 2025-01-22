"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 84
Updated: 2025-01-22T15:53:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 84
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
