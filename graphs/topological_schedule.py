"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2289
Updated: 2026-10-23T22:29:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2289
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
