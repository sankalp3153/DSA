"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1139
Updated: 2025-11-16T18:36:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1139
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
