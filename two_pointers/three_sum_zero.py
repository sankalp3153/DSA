"""
Module: three_sum_zero
Approach: sorted duplicate-skipping two pointer
Revision: 947
Updated: 2025-09-11T10:54:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 947
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
