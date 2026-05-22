"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1790
Updated: 2026-05-22T22:36:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1790
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
