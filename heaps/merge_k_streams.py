"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 501
Updated: 2025-05-10T14:13:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 501
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
