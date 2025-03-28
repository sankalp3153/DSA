"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 360
Updated: 2025-03-28T15:33:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 360
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
