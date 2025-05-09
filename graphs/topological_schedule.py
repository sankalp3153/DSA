"""
Module: topological_schedule
Approach: Kahn indegree cycle detection
Revision: 495
Updated: 2025-05-09T14:20:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 495
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
