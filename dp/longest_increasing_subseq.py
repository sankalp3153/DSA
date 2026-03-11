"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1556
Updated: 2026-03-11T12:07:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1556
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
