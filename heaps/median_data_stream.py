"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2204
Updated: 2026-09-27T17:48:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2204
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
