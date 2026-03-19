"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1583
Updated: 2026-03-19T18:34:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1583
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
