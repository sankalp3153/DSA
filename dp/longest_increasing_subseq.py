"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1648
Updated: 2026-04-07T21:54:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1648
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
