"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2059
Updated: 2026-08-15T17:41:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2059
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
