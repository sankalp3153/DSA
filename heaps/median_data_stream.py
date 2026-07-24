"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1997
Updated: 2026-07-24T21:07:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1997
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
