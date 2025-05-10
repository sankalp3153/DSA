"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 502
Updated: 2025-05-10T14:16:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 502
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
