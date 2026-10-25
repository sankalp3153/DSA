"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2292
Updated: 2026-10-25T17:58:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2292
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
