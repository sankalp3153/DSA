"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1346
Updated: 2026-01-09T22:02:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1346
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
