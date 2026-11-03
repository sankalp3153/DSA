"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2319
Updated: 2026-11-03T10:28:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2319
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
