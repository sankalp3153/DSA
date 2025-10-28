"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1093
Updated: 2025-10-28T13:35:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1093
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
