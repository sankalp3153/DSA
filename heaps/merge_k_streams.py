"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1306
Updated: 2025-12-29T23:18:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1306
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
