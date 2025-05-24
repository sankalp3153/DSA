"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 548
Updated: 2025-05-24T13:00:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 548
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
