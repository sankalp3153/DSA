"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 58
Updated: 2025-01-11T14:07:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 58
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
