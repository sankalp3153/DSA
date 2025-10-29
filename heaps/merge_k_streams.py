"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1099
Updated: 2025-10-29T14:03:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1099
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
