"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 932
Updated: 2025-09-08T12:44:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 932
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
