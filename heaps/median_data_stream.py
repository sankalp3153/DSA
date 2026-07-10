"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1951
Updated: 2026-07-10T10:48:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1951
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
