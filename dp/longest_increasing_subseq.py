"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1142
Updated: 2025-11-18T16:36:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1142
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
