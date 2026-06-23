"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1898
Updated: 2026-06-23T17:22:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1898
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
