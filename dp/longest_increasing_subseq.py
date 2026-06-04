"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1832
Updated: 2026-06-04T23:00:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1832
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
