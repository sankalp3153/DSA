"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 547
Updated: 2025-05-24T12:46:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 547
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
