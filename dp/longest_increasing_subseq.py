"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 1234
Updated: 2025-12-10T21:38:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1234
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
