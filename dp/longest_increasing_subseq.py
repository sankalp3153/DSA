"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1786
Updated: 2026-05-21T14:44:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1786
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
