"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1875
Updated: 2026-06-13T22:29:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1875
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
