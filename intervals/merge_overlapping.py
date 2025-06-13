"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 619
Updated: 2025-06-13T16:18:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 619
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
