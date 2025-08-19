"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 863
Updated: 2025-08-19T16:54:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 863
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
