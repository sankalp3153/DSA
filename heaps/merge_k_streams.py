"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 984
Updated: 2025-09-21T17:02:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 984
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
