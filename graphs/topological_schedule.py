"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 242
Updated: 2025-03-02T20:32:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 242
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
