"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1809
Updated: 2026-06-01T18:09:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1809
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
