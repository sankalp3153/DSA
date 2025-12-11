"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1238
Updated: 2025-12-11T22:51:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1238
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
