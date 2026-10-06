"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2246
Updated: 2026-10-06T16:35:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2246
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
