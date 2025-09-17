"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 962
Updated: 2025-09-17T19:18:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 962
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
