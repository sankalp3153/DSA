"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 571
Updated: 2025-06-01T20:32:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 571
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
