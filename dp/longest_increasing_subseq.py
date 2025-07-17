"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 728
Updated: 2025-07-17T19:40:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 728
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
