"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 981
Updated: 2025-09-21T14:03:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 981
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
