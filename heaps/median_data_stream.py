"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 226
Updated: 2025-02-25T17:37:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 226
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
