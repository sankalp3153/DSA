"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1192
Updated: 2025-12-01T10:04:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1192
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
