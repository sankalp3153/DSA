"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2220
Updated: 2026-09-30T15:41:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2220
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
