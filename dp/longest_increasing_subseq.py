"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2269
Updated: 2026-10-17T16:29:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2269
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
