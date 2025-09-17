"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 961
Updated: 2025-09-17T18:14:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 961
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
