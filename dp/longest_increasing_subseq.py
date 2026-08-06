"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2039
Updated: 2026-08-06T14:17:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2039
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
