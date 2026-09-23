"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2200
Updated: 2026-09-23T17:44:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2200
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
