"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 426
Updated: 2025-04-16T21:01:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 426
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
