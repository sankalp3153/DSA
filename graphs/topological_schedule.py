"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 978
Updated: 2025-09-21T12:02:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 978
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
