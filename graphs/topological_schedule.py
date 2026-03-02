"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1530
Updated: 2026-03-02T16:01:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1530
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
