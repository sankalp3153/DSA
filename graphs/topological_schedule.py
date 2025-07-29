"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 771
Updated: 2025-07-29T14:23:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 771
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
