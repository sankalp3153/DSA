"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 311
Updated: 2025-03-18T11:29:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 311
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
