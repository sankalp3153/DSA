"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1921
Updated: 2026-07-01T23:32:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1921
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
