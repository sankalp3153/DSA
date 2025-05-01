"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 472
Updated: 2025-05-01T11:16:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 472
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
