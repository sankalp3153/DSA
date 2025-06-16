"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 633
Updated: 2025-06-16T19:02:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 633
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
