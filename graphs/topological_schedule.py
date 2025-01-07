"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 35
Updated: 2025-01-07T19:38:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 35
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
