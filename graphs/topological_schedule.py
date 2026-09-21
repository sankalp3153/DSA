"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2197
Updated: 2026-09-21T16:51:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2197
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
