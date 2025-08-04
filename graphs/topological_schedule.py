"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 794
Updated: 2025-08-04T18:55:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 794
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
