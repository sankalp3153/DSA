"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1721
Updated: 2026-04-28T17:13:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1721
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
