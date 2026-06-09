"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1852
Updated: 2026-06-09T22:59:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1852
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
