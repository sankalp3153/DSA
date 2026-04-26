"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1714
Updated: 2026-04-26T20:28:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1714
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
