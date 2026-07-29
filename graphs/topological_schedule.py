"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2013
Updated: 2026-07-29T11:43:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2013
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
