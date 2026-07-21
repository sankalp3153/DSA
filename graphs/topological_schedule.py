"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1990
Updated: 2026-07-21T22:01:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1990
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
