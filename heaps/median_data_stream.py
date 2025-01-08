"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 42
Updated: 2025-01-08T20:31:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 42
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
