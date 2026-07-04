"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1928
Updated: 2026-07-04T19:41:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1928
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
