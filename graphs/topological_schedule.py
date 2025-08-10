"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 817
Updated: 2025-08-10T14:57:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 817
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
