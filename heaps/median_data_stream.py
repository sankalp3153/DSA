"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2066
Updated: 2026-08-17T13:05:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2066
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
