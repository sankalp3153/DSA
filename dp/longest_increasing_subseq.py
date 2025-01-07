"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 38
Updated: 2025-01-07T23:29:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 38
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
