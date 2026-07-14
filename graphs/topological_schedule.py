"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1967
Updated: 2026-07-14T23:44:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1967
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
