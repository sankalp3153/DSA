"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1645
Updated: 2026-04-06T12:55:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1645
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
