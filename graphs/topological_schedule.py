"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1300
Updated: 2025-12-29T12:20:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1300
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
