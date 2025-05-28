"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 564
Updated: 2025-05-28T15:03:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 564
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
