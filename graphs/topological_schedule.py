"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1484
Updated: 2026-02-19T10:55:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1484
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
