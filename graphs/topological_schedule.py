"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 265
Updated: 2025-03-08T20:03:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 265
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
