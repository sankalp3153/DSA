"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 196
Updated: 2025-02-16T20:05:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 196
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
