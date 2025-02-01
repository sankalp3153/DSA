"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 134
Updated: 2025-02-01T10:30:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 134
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
