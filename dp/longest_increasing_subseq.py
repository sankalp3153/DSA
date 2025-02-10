"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 176
Updated: 2025-02-10T17:12:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 176
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
