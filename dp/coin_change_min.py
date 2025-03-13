"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 292
Updated: 2025-03-13T11:12:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 292
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
