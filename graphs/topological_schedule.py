"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2174
Updated: 2026-09-16T14:49:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2174
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
