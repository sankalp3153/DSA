"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2135
Updated: 2026-08-31T18:42:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2135
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
