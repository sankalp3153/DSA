"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1054
Updated: 2025-10-14T21:33:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1054
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
