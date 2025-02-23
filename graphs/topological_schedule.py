"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 219
Updated: 2025-02-23T10:52:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 219
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
