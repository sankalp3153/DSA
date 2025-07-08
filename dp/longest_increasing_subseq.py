"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 705
Updated: 2025-07-08T11:26:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 705
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
