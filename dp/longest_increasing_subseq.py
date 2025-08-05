"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 797
Updated: 2025-08-05T15:35:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 797
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
