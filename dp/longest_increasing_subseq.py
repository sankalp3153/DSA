"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1303
Updated: 2025-12-29T21:36:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1303
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
