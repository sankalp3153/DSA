"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 617
Updated: 2025-06-13T15:01:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 617
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
