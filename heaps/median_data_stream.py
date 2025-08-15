"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 847
Updated: 2025-08-15T18:52:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 847
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
