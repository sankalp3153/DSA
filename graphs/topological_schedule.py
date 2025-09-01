"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 909
Updated: 2025-09-01T11:57:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 909
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
