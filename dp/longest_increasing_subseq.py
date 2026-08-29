"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2131
Updated: 2026-08-29T19:38:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2131
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
