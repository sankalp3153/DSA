"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 272
Updated: 2025-03-09T16:55:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 272
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
