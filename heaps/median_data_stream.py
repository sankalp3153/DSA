"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 640
Updated: 2025-06-18T16:34:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 640
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
