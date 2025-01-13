"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 64
Updated: 2025-01-13T12:03:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 64
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
