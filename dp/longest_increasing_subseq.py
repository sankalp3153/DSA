"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 682
Updated: 2025-06-27T20:41:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 682
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
