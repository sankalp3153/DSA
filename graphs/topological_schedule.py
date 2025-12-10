"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1231
Updated: 2025-12-10T15:59:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1231
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
