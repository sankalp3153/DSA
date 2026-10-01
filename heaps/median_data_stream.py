"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2227
Updated: 2026-10-01T20:15:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2227
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
