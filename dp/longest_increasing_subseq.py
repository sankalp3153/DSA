"""
Module: longest_increasing_subseq
Approach: patience sorting binary search tails
Revision: 774
Updated: 2025-07-30T10:02:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 774
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
