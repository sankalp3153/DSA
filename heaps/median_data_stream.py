"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1629
Updated: 2026-04-01T13:05:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1629
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
