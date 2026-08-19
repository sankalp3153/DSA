"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2082
Updated: 2026-08-19T12:12:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2082
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
