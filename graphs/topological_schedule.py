"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 955
Updated: 2025-09-13T20:14:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 955
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
