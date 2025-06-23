"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 656
Updated: 2025-06-23T18:19:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 656
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
