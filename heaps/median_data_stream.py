"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1560
Updated: 2026-03-12T20:26:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1560
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
