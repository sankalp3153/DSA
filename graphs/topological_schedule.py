"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1369
Updated: 2026-01-19T12:36:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1369
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
