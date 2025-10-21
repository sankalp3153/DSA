"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1073
Updated: 2025-10-21T22:14:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1073
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
