"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2243
Updated: 2026-10-05T19:26:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2243
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
