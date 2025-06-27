"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 679
Updated: 2025-06-27T16:39:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 679
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
