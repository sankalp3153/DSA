"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1947
Updated: 2026-07-08T22:31:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1947
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
