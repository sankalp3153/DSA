"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1077
Updated: 2025-10-23T13:12:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1077
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
