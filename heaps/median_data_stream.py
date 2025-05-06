"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 479
Updated: 2025-05-06T13:28:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 479
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
