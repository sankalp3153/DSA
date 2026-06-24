"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1905
Updated: 2026-06-24T19:50:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1905
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
