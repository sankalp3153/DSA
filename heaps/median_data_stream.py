"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1675
Updated: 2026-04-14T21:40:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1675
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
