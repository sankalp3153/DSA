"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2036
Updated: 2026-08-05T19:18:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2036
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
