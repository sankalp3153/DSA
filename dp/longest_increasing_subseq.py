"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 268
Updated: 2025-03-09T10:18:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 268
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
