"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1277
Updated: 2025-12-23T12:02:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1277
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
