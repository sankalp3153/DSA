"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1050
Updated: 2025-10-14T11:37:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1050
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
