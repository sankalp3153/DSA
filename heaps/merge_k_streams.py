"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 639
Updated: 2025-06-18T13:57:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 639
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
