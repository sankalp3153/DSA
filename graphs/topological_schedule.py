"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 840
Updated: 2025-08-15T10:10:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 840
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
