"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2020
Updated: 2026-07-31T14:35:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2020
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
