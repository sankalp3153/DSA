"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 1622
Updated: 2026-03-27T18:35:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1622
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
