"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 708
Updated: 2025-07-11T11:13:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 708
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
