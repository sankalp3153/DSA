"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1284
Updated: 2025-12-23T23:44:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1284
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
