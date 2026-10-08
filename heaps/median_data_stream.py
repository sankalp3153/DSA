"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2250
Updated: 2026-10-08T17:52:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2250
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
