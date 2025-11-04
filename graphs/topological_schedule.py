"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1116
Updated: 2025-11-04T10:24:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1116
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
