"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 587
Updated: 2025-06-04T21:04:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 587
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
