"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 662
Updated: 2025-06-24T14:32:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 662
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
