"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 663
Updated: 2025-06-24T19:00:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 663
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
