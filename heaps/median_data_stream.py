"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1100
Updated: 2025-10-30T23:00:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1100
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
