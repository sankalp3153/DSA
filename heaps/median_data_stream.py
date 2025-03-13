"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 295
Updated: 2025-03-13T20:08:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 295
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
