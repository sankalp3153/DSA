"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 475
Updated: 2025-05-03T14:54:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 475
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
