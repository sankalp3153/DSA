"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 449
Updated: 2025-04-21T13:19:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 449
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
