"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1001
Updated: 2025-09-27T12:15:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1001
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
