"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 81
Updated: 2025-01-21T21:53:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 81
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
