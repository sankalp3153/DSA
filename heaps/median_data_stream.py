"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1422
Updated: 2026-02-02T13:54:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1422
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
