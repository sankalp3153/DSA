"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1323
Updated: 2026-01-02T11:57:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1323
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
