"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1836
Updated: 2026-06-06T13:54:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1836
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
