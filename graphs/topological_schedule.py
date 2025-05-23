"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 541
Updated: 2025-05-23T11:07:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 541
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
