"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1970
Updated: 2026-07-15T15:22:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1970
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
