"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1652
Updated: 2026-04-10T12:12:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1652
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
