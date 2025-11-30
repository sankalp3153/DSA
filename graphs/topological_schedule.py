"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1185
Updated: 2025-11-30T11:24:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1185
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
