"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 456
Updated: 2025-04-23T21:44:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 456
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
