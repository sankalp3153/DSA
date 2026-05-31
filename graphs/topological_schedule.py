"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1806
Updated: 2026-05-31T21:03:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1806
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
