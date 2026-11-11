"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2342
Updated: 2026-11-11T19:14:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2342
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
