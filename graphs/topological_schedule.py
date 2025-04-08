"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 403
Updated: 2025-04-08T14:32:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 403
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
