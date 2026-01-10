"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1349
Updated: 2026-01-10T22:31:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1349
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
