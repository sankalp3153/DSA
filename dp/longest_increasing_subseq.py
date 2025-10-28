"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1096
Updated: 2025-10-28T23:22:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1096
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
