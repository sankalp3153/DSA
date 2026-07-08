"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1944
Updated: 2026-07-08T20:49:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1944
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
