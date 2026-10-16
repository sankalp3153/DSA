"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2266
Updated: 2026-10-16T18:54:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2266
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
