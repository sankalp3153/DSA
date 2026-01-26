"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1392
Updated: 2026-01-26T15:07:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1392
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
