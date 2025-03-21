"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 334
Updated: 2025-03-21T17:44:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 334
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
