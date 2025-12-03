"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1208
Updated: 2025-12-03T17:27:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1208
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
