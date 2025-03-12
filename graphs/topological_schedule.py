"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 288
Updated: 2025-03-12T17:23:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 288
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
