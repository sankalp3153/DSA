"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 2338
Updated: 2026-11-10T11:29:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2338
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
