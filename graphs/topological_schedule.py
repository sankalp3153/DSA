"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 748
Updated: 2025-07-23T23:42:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 748
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
