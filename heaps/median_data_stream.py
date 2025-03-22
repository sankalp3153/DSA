"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 341
Updated: 2025-03-22T13:22:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 341
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
