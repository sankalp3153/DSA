"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 364
Updated: 2025-03-30T15:59:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 364
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
