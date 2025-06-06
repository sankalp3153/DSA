"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 594
Updated: 2025-06-06T20:19:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 594
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
