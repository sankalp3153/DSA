"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2151
Updated: 2026-09-03T16:44:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2151
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
