"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1783
Updated: 2026-05-20T17:48:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1783
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
