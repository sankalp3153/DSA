"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1668
Updated: 2026-04-12T11:33:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1668
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
