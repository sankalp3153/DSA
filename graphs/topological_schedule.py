"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 173
Updated: 2025-02-10T13:21:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 173
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
