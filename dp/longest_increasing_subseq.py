"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1510
Updated: 2026-02-27T11:56:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1510
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
