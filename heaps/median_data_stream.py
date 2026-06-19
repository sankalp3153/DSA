"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1882
Updated: 2026-06-19T14:35:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1882
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
