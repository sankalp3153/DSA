"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1698
Updated: 2026-04-18T21:24:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1698
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
