"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 938
Updated: 2025-09-09T12:27:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 938
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
