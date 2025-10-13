"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1047
Updated: 2025-10-13T14:27:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1047
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
