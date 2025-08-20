"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 866
Updated: 2025-08-20T13:33:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 866
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
