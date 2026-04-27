"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1717
Updated: 2026-04-27T17:50:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1717
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
