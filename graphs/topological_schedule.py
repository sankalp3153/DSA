"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1024
Updated: 2025-10-06T10:20:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1024
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
