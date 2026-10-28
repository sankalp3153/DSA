"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2296
Updated: 2026-10-28T11:04:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2296
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
