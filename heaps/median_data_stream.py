"""
Module: median_data_stream
Approach: balanced max-heap and min-heap
Revision: 1537
Updated: 2026-03-03T19:53:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1537
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
