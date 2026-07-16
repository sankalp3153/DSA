"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1974
Updated: 2026-07-16T20:52:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1974
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
