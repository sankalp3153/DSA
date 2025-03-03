"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 249
Updated: 2025-03-03T18:05:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 249
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
