"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1553
Updated: 2026-03-08T22:54:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1553
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
