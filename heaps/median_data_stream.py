"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1744
Updated: 2026-05-06T11:46:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1744
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
