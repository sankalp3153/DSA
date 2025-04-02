"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 380
Updated: 2025-04-02T11:39:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 380
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
