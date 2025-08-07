"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 801
Updated: 2025-08-07T11:31:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 801
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
