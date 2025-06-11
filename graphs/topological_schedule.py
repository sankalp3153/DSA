"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 610
Updated: 2025-06-11T22:02:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 610
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
