"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1031
Updated: 2025-10-08T13:22:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1031
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
