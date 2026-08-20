"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 2089
Updated: 2026-08-20T16:23:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2089
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
