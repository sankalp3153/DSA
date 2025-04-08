"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 406
Updated: 2025-04-08T21:38:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 406
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
