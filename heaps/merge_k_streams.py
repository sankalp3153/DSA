"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1444
Updated: 2026-02-07T13:44:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1444
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
