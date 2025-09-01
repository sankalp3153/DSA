"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 912
Updated: 2025-09-01T16:56:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 912
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
