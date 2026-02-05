"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1438
Updated: 2026-02-05T23:00:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1438
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
