"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1123
Updated: 2025-11-07T19:51:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1123
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
