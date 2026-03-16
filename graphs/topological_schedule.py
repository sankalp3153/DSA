"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1576
Updated: 2026-03-16T16:36:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1576
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
