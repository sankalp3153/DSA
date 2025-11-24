"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1162
Updated: 2025-11-24T13:16:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1162
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
