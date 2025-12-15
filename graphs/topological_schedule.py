"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1254
Updated: 2025-12-15T10:54:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1254
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
