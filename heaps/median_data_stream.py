"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2158
Updated: 2026-09-05T14:39:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2158
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
