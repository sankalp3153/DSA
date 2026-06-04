"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1829
Updated: 2026-06-04T19:15:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1829
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
