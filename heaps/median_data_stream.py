"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 433
Updated: 2025-04-17T16:47:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 433
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
