"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 150
Updated: 2025-02-03T21:03:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 150
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
