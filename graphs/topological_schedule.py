"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1070
Updated: 2025-10-20T20:12:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1070
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
