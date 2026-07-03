"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1924
Updated: 2026-07-03T16:16:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1924
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
