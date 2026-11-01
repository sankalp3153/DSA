"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2312
Updated: 2026-11-01T10:12:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2312
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
