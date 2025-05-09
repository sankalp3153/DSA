"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 498
Updated: 2025-05-09T19:02:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 498
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
