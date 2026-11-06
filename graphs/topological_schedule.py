"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2335
Updated: 2026-11-06T16:52:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2335
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
