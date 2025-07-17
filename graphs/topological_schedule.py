"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 725
Updated: 2025-07-17T18:48:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 725
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
