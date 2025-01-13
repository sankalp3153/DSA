"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 65
Updated: 2025-01-13T12:38:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 65
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
