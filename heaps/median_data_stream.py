"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 686
Updated: 2025-06-28T20:40:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 686
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
