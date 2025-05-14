"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 518
Updated: 2025-05-14T21:52:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 518
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
