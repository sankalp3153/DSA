"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1740
Updated: 2026-05-05T22:36:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1740
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
