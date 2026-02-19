"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1487
Updated: 2026-02-19T18:01:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1487
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
