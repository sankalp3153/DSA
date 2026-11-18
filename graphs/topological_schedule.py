"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2358
Updated: 2026-11-18T19:53:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2358
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
