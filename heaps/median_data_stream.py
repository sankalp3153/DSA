"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 709
Updated: 2025-07-12T11:09:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 709
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
