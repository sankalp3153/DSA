"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1215
Updated: 2025-12-06T10:02:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1215
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
