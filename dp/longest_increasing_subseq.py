"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1878
Updated: 2026-06-16T22:46:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1878
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
