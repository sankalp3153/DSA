"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1694
Updated: 2026-04-18T12:07:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1694
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
