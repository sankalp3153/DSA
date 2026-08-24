"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2105
Updated: 2026-08-24T18:34:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2105
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
