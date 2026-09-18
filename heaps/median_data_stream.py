"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2181
Updated: 2026-09-18T17:55:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2181
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
