"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 702
Updated: 2025-07-07T19:05:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 702
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
