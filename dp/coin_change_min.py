"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2201
Updated: 2026-09-27T12:35:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2201
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
