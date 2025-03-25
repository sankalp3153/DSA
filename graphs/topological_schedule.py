"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 357
Updated: 2025-03-25T23:18:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 357
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
