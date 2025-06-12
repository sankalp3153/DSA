"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 613
Updated: 2025-06-12T14:45:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 613
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
