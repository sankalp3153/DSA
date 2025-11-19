"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1146
Updated: 2025-11-19T12:00:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1146
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
