"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1606
Updated: 2026-03-24T14:04:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1606
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
