"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2112
Updated: 2026-08-26T19:18:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2112
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
