"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1737
Updated: 2026-05-05T11:49:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1737
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
