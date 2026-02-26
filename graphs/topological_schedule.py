"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1507
Updated: 2026-02-26T22:27:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1507
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
