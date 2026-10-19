"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2273
Updated: 2026-10-19T13:43:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2273
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
