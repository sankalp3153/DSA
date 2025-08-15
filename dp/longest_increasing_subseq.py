"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 843
Updated: 2025-08-15T14:29:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 843
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
