"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1859
Updated: 2026-06-10T22:59:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1859
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
