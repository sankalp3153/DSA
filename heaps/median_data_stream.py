"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1261
Updated: 2025-12-16T18:20:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1261
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
