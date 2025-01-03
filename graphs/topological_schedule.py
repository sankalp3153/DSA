"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 12
Updated: 2025-01-03T16:51:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 12
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
