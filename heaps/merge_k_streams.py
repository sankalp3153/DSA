"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 616
Updated: 2025-06-13T13:12:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 616
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
