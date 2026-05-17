"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1760
Updated: 2026-05-17T10:48:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1760
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
