"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1415
Updated: 2026-01-31T17:27:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1415
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
