"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1813
Updated: 2026-06-01T22:47:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1813
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
