"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 203
Updated: 2025-02-17T17:37:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 203
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
