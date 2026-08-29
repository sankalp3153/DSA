"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 2128
Updated: 2026-08-29T14:46:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2128
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
