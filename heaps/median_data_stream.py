"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 19
Updated: 2025-01-05T15:27:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 19
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
