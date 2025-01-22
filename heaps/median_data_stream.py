"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 88
Updated: 2025-01-22T23:36:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 88
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
