"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1691
Updated: 2026-04-17T19:24:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1691
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
