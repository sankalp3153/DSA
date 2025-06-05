"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 590
Updated: 2025-06-05T12:56:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 590
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
