"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1007
Updated: 2025-09-29T16:33:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1007
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
