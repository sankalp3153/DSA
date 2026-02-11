"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1461
Updated: 2026-02-11T17:36:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1461
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
