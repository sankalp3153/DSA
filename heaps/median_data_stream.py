"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 157
Updated: 2025-02-06T13:04:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 157
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
