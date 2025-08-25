"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 886
Updated: 2025-08-25T15:34:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 886
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
