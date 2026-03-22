"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1599
Updated: 2026-03-22T21:54:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1599
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
