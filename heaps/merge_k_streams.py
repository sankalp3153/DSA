"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1605
Updated: 2026-03-24T13:56:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1605
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
