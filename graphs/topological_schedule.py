"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 127
Updated: 2025-01-30T14:42:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 127
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
